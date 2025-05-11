# RAG-a-Doodle-Doo
> <h3>A simple knowledge assistant that does Retrieval, Generation and Orchestration</h3>

## 📁 Project Structure
```
RAG-a-Doodle-Doo/
├── data/                # Stores raw text files and optionally the vector store
│   ├── doc1.txt
│   └── ...
├── agent.py             # Query router: decides between RAG and Tool logic
├── retriever.py         # Handles embedding, indexing, and retrieval
├── llm.py               # Interfaces with the LLM (OpenAI or similar)
├── tools.py             # Handles tool-based queries (calculate/define)
├── app.py               # Main file to run the app (CLI or Streamlit)
└── requirements.txt     # Dependencies
```

## 🛠️ Installation Guide

### 1. Clone the Repository

```bash
git clone https://github.com/HarshalLoya/RAG-a-Doodle-Doo.git
cd RAG-a-Doodle-Doo
```

### 2. (Optional) Create a Virtual Environment

```bash
python -m venv venv

# Activate on Unix/macOS:
source venv/bin/activate

# Activate on Windows:
venv\Scripts\activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

⚠️ **Note**: If PyTorch installation fails, install it manually with (for CUDA 12.8):

```bash
pip install torch --index-url https://download.pytorch.org/whl/cu128
```

### 4. Set Up Your API Key

Export your LLM API key as an environment variable:

```bash
# Unix/macOS:
export GROQ_LLAMA_70B_VERSATILE_API_KEY=<YOUR_API_KEY>

# Windows:
set GROQ_LLAMA_70B_VERSATILE_API_KEY=<YOUR_API_KEY>
```

---
