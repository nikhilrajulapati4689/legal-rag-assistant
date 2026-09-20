# ⚖ Legal Document RAG Assistant

A Retrieval-Augmented Generation (RAG) based legal document assistant that retrieves relevant information from legal PDF documents and generates grounded answers with source citations.

> **Educational Information Retrieval System — Not Legal Advice**
>
> This project is intended for educational and informational purposes only. It does not provide legal advice or professional legal services.

---

## 📌 Overview

Legal documents can be lengthy and difficult to search manually. This project allows users to ask questions in natural language and retrieve relevant information from a predefined collection of legal documents.

The system combines:

- PDF text extraction
- Text chunking
- Sentence embeddings
- FAISS vector search
- Google Gemini
- Flask web interface
- Source and page citations

---

## 🏗️ System Architecture

```text
Legal PDF Documents
        ↓
PDF Text Extraction
        ↓
Text Chunking
        ↓
Embedding Generation
        ↓
FAISS Vector Store
        ↓
User Question
        ↓
Query Embedding
        ↓
Semantic Search
        ↓
Relevant Document Chunks
        ↓
Gemini LLM
        ↓
Grounded Answer + Source Citation
```

---

## ✨ Features

- 📄 PDF document ingestion
- ✂️ Text chunking with overlap
- 🧠 Sentence-transformer embeddings
- 🔎 Semantic vector search using FAISS
- 🎯 Relevance threshold
- 🤖 Gemini-based answer generation
- 📚 Source file and page citations
- 🚫 "Information not found" handling
- 🌐 Flask web application
- 💬 Chat-style interface
- 🧹 Clear Chat functionality
- 💻 Terminal-based interface

---

## 🛠️ Technologies

| Technology | Purpose |
|---|---|
| Python | Core development |
| PyMuPDF | PDF text extraction |
| Sentence Transformers | Embeddings |
| FAISS | Vector similarity search |
| Google Gemini | Answer generation |
| Flask | Web backend |
| HTML/CSS/JavaScript | User interface |
| python-dotenv | Environment variables |

---

## 🧠 How RAG Works

When a user asks a question:

1. The question is converted into an embedding.
2. FAISS searches for similar document chunks.
3. The most relevant chunks are retrieved.
4. A relevance threshold filters unsupported results.
5. Retrieved content is provided to Gemini.
6. Gemini generates an answer using the retrieved content.
7. The response includes the source document and page number.

If relevant information cannot be found, the system responds:

```text
Information not found in the provided legal documents.
```

---

## 📁 Project Structure

```text
legal-rag-assistant/
│
├── documents/
│   ├── sample.pdf
│   └── second_document.pdf
│
├── src/
│   ├── __init__.py
│   ├── answer_generator.py
│   ├── embedder.py
│   ├── index_documents.py
│   ├── pdf_loader.py
│   ├── rag_pipeline.py
│   ├── retriever.py
│   ├── test_config.py
│   └── vector_store.py
│
├── templates/
│   └── index.html
│
├── vectorstore/
│   ├── legal.index
│   └── metadata.pkl
│
├── web/
│   └── app.py
│
├── main.py
├── .gitignore
└── README.md
```

---

## ⚙️ Installation

### 1. Clone the Repository

```bash
git clone https://github.com/nikhilrajulapati4689/legal-rag-assistant.git
cd legal-rag-assistant
```

### 2. Create Virtual Environment

```bash
python -m venv venv
```

For Windows PowerShell:

```powershell
venv\Scripts\Activate.ps1
```

### 3. Install Dependencies

```bash
pip install pymupdf
pip install sentence-transformers
pip install faiss-cpu
pip install google-genai
pip install python-dotenv
pip install flask
```

---

## 🔑 API Configuration

Create a `.env` file in the project root:

```text
GEMINI_API_KEY=your_api_key_here
```

The `.env` file is excluded from Git using `.gitignore`.

**Never upload your API key to GitHub.**

---

## ▶️ Run the Web Application

Start Flask:

```bash
python web/app.py
```

Open:

```text
http://127.0.0.1:5000
```

---

## 💻 Run the Terminal Application

```bash
python main.py
```

Type:

```text
exit
```

to close the application.

---

## 📚 Add New Documents

Place permitted PDF files inside:

```text
documents/
```

Then rebuild the vector index:

```bash
python src/index_documents.py
```

---

## 📊 Current Configuration

```text
Embedding Model : all-MiniLM-L6-v2
Embedding Size  : 384
Chunk Size      : 1000 characters
Chunk Overlap   : 200 characters
Top-K Retrieval : 3
Distance Limit  : 1.2
```

---

## 🛡️ Hallucination Reduction

The system attempts to reduce unsupported answers through:

- Document-grounded generation
- Restricted prompts
- Semantic retrieval
- Relevance filtering
- Source citations
- "Information not found" handling

---

## ⚠️ Limitations

- Answers are limited to the indexed document collection.
- Retrieval quality depends on document quality and chunking.
- Character-based chunking may split legal sections.
- The relevance threshold may require tuning.
- Scanned PDFs may require OCR.
- Gemini API usage is subject to API limits.
- The system is not a substitute for professional legal advice.

---

## 🚀 Future Enhancements

- Legal-aware document chunking
- OCR support
- Hybrid keyword + vector search
- Retrieval evaluation metrics
- Improved citation formatting
- Document upload through the web interface
- Authentication
- Automated testing
- Improved UI and accessibility

---

## 🎓 Academic Purpose

This project demonstrates the practical application of:

- Retrieval-Augmented Generation (RAG)
- Natural Language Processing
- Semantic Search
- Vector Databases
- Sentence Embeddings
- Large Language Models
- Grounded Question Answering
- Source Citation
- Hallucination Reduction

---

## ⚖️ Disclaimer

**Educational Information Retrieval System — Not Legal Advice.**

This application is intended solely for educational and informational purposes. Information generated by the system should not be considered legal advice, legal opinion, or professional legal service.

For legal decisions, consult a qualified legal professional.

---

## 📌 Repository

[GitHub Repository](https://github.com/nikhilrajulapati4689/legal-rag-assistant)
