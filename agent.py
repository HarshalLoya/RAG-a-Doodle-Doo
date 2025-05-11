from typing import Dict, List
from retriever import retrieve
from llm import answer as llm_answer
from tools import calculate, define
import warnings
warnings.filterwarnings('ignore')

# Keywords to detect tool-based queries
CALC_KEYWORDS = {"calculate", "compute", "eval", "evaluate"}
DEFINE_KEYWORDS = {"define", "what is", "meaning of"}


def is_calculation_query(query: str) -> bool:
    q = query.lower()
    return any(q.startswith(k) or k in q for k in CALC_KEYWORDS)


def is_definition_query(query: str) -> bool:
    q = query.lower()
    return any(q.startswith(k) or k in q for k in DEFINE_KEYWORDS)


def handle_query(query: str) -> Dict:
    """
    Routes the incoming query to either:
      - tools.calculate / tools.define
      - RAG pipeline (retriever + LLM)
    Returns a dict with:
      - 'branch': 'tool' or 'rag'
      - 'context': list of chunks (only for RAG)
      - 'answer': final answer string
    """
    # 1) Tool branch
    if is_calculation_query(query):
        result = calculate(query)
        return {"branch": "tool", "context": [], "answer": result}

    if is_definition_query(query):
        result = define(query)
        return {"branch": "tool", "context": [], "answer": result}

    # 2) RAG branch
    context_chunks = retrieve(query)
    result = llm_answer(query, context_chunks)
    return {"branch": "rag", "context": context_chunks, "answer": result}


# CLI test harness
if __name__ == "__main__":
    print("🧠 RAG-Agent REPL. Type 'exit' to quit.")
    while True:
        q = input("\nQuestion: ").strip()
        if q.lower() in ("exit", "quit"):
            break

        response = handle_query(q)
        print(f"\n> Branch: {response['branch'].upper()}")
        if response["branch"] == "rag":
            print("\nRetrieved Context:")
            for c in response["context"]:
                print(
                    f" - [{c['score']:.4f}] {c['doc_id']}#{c['chunk_idx']}: {c['text'][:100]}..."
                )
        print(f"\nAnswer:\n{response['answer']}\n")
