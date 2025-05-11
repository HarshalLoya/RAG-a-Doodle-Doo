# RAG-a-Doodle-Doo
> <h3>A simple knowledge assistant that does Retrieval, Generation and Orchestration</h3>

---

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
└── requirements.txt     # Dependencies
```

---

## Key Design Choices

- **Single Data Directory**: All documents and index files live under `data/` for simplicity.  
- **Four Core Modules**:  
  - `retriever.py` for chunking + FAISS retrieval  
  - `llm.py` for LLM calls via Groq’s OpenAI-compatible API  
  - `tools.py` for specialized “calculate” and “define” logic  
  - `agent.py` to unify routing and orchestrate both paths  
- **Groq API + LLaMA 3.3-70B**: Fast, high-quality inference without local model downloads.  
- **Chunking Strategy**: Word-based sliding windows (400 words, 200 overlap) to balance context coverage and index size.  
- **Safe Eval**: Restricted `eval()` environment in `calculate()` to prevent arbitrary code execution.

---

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
## 🚀 Run the App


```bash
python retriever.py
python retriever.py rebuild
python agent.py
```

---

## 📜 License

This project is licensed under the MIT License.  
See the [LICENSE](LICENSE) file for details.

---

## 🤝 Contributing

Contributions, issues, and feature requests are welcome!  
Feel free to fork the repo, open issues, or submit pull requests.