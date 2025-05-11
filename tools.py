import re
from llm import answer as llm_answer


def calculate(query: str) -> str:
    try:
        # Extract everything after the keyword "calculate"/"evaluate"
        expression = re.sub(
            r"(calculate|compute|evaluate|eval)", "", query, flags=re.IGNORECASE
        ).strip()
        result = eval(expression, {"__builtins__": {}}, {})
        return f"The result is {result}"
    except Exception as e:
        return f"Could not evaluate expression: {e}"


def define(query: str) -> str:
    # Try to extract term from 'define X' or 'what is X'
    match = re.search(
        r"(?:define|what is|meaning of)\s+(.*)", query, flags=re.IGNORECASE
    )
    term = match.group(1).strip() if match else query.strip()

    define_prompt = f"Define the following term in simple words: {term}"
    return llm_answer(define_prompt, context_chunks=[])
