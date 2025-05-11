import os
import openai
from typing import List, Dict
from dotenv import load_dotenv

load_dotenv()


client = openai.OpenAI(
    base_url="https://api.groq.com/openai/v1",
    api_key=os.getenv("GROQ_LLAMA_70B_VERSATILE_API_KEY"),
)
MODEL_NAME = "llama3-70b-8192"


def _build_rag_prompt(query: str, context_chunks: List[Dict]) -> str:
    snippets = [
        f"[{i}] ({c['doc_id']}#{c['chunk_idx']}): {c['text']}"
        for i, c in enumerate(context_chunks, start=1)
    ]
    return (
        "Use the following context to answer the question.\n\n"
        f"Context:\n{'\n'.join(snippets)}\n\n"
        f"Question: {query}"
    )


def answer(query: str, context_chunks: List[Dict]) -> str:
    prompt = _build_rag_prompt(query, context_chunks)
    response = client.chat.completions.create(
        model=MODEL_NAME,
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": prompt},
        ],
        temperature=0.0,
        max_tokens=512,
    )
    return response.choices[0].message.content.strip()


# Optional test run
if __name__ == "__main__":
    sample_chunks = [
        {
            "doc_id": "python_data_structures.txt",
            "chunk_idx": 0,
            "text": "Lists are ordered, mutable sequences. Tuples are ordered but immutable.",
            "score": 0.97,
        }
    ]
    q = "What is the difference between a list and a tuple in Python?"
    print(answer(q, sample_chunks))
