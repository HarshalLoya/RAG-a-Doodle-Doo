import os
import glob
import faiss
import numpy as np
from typing import List, Tuple, Dict
from sentence_transformers import SentenceTransformer
import warnings

warnings.filterwarnings("ignore")

DATA_DIR = "data"
INDEX_PATH = os.path.join(DATA_DIR, "index.faiss")
METADATA_PATH = os.path.join(DATA_DIR, "metadata.npy")
MODEL_NAME = "jinaai/jina-embeddings-v3"
CHUNK_SIZE = 400
OVERLAP = 200
EMBEDDING_DIM = 768

_model = SentenceTransformer(MODEL_NAME, trust_remote_code=True)


def load_documents(data_dir: str = DATA_DIR) -> List[Tuple[str, str]]:
    """
    Reads all .txt files under data_dir.
    Returns list of (doc_id, text).
    """
    docs = []
    for path in glob.glob(os.path.join(data_dir, "*.txt")):
        doc_id = os.path.basename(path)
        with open(path, "r", encoding="utf-8") as f:
            text = f.read()
        docs.append((doc_id, text))
    return docs


def chunk_document(
    text: str, chunk_size: int = CHUNK_SIZE, overlap: int = OVERLAP
) -> List[Tuple[int, str]]:
    """
    Splits `text` into overlapping word-based chunks.
    Returns list of (chunk_idx, chunk_text).
    """
    words = text.split()
    chunks = []
    start = 0
    idx = 0
    while start < len(words):
        end = start + chunk_size
        chunk_words = words[start:end]
        chunks.append((idx, " ".join(chunk_words)))
        idx += 1
        start += chunk_size - overlap
    return chunks


def embed_chunks(chunk_texts: List[str]) -> np.ndarray:
    """
    Returns embeddings array for a list of chunk texts.
    Shape = (n_chunks, EMBEDDING_DIM)
    """
    return _model.encode(
        chunk_texts,
        show_progress_bar=True,
        convert_to_numpy=True,
        batch_size=16,
        normalize_embeddings=True,
        model_args={"task": "retrieval.passage"},
    )


def build_faiss_index(
    embeddings: np.ndarray, metadata: List[Dict], index_path: str = INDEX_PATH
) -> None:
    """
    Builds a FAISS Flat index, adds embeddings,
    and saves index + metadata to disk.
    """
    # 1) Create index
    index = faiss.IndexFlatIP(
        embeddings.shape[1]
    )  # inner product (cosine after normalization)
    # 2) Add vectors
    index.add(embeddings)
    # 3) Persist
    faiss.write_index(index, index_path)
    # 4) Save metadata (parallel array to embeddings)
    np.save(METADATA_PATH, np.array(metadata, dtype=object))
    print(f"[+] FAISS index saved to {index_path}")
    print(f"[+] Metadata saved to {METADATA_PATH}")


def retrieve(query: str, index_path: str = INDEX_PATH, top_k: int = 3) -> List[Dict]:
    """
    Embeds the query, searches the FAISS index,
    and returns top_k chunks with their scores.
    """
    # 1) Embed query
    q_emb = _model.encode(
        [query],
        convert_to_numpy=True,
        normalize_embeddings=True,
        model_args={"task": "retrieval.query"},
    )
    # 2) Load index & metadata
    index = faiss.read_index(index_path)
    metadata = np.load(METADATA_PATH, allow_pickle=True)
    # 3) Search
    D, I = index.search(q_emb, top_k)
    results = []
    for score, idx in zip(D[0], I[0]):
        if idx < len(metadata):
            md = metadata[idx]
            results.append(
                {
                    "doc_id": md["doc_id"],
                    "chunk_idx": md["chunk_idx"],
                    "text": md["text"],
                    "score": float(score),
                }
            )
    return results


def rebuild_index():
    """
    Helper to load docs, chunk, embed, and build the FAISS index.
    """
    docs = load_documents()
    all_texts = []
    metadata = []
    for doc_id, text in docs:
        chunks = chunk_document(text)
        for idx, chunk in chunks:
            all_texts.append(chunk)
            metadata.append({"doc_id": doc_id, "chunk_idx": idx, "text": chunk})
    embeddings = embed_chunks(all_texts)
    build_faiss_index(embeddings, metadata)


if __name__ == "__main__":
    import sys

    if len(sys.argv) < 2:
        print('Usage: python retriever.py [rebuild|query] ["your query"]')
        sys.exit(1)

    cmd = sys.argv[1]
    if cmd == "rebuild":
        rebuild_index()
    elif cmd == "query" and len(sys.argv) == 3:
        q = sys.argv[2]
        for r in retrieve(q):
            print(f"[{r['score']:.4f}] {r['doc_id']}#{r['chunk_idx']}: {r['text']}")
    else:
        print("Invalid command.")
