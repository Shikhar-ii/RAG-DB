# RAG-DB
# RagDB

**RagDB** is a lightweight **Retrieval-Augmented Generation (RAG)** system designed to retrieve concise answers from uploaded documents. It converts documents into embeddings, stores them in a vector database, and retrieves the most relevant sections when a user asks a question.

The goal of RagDB is to provide a **simple, modular starting point** for developers building document-aware AI systems such as research assistants, knowledge bases, or internal document search tools.

---

## Features

* Upload and index **PDF documents**
* Automatic **text extraction**
* Smart **chunking with overlap**
* Semantic search using **sentence embeddings**
* **FAISS vector database** for fast retrieval
* Generate **brief answers** from relevant document sections
* Minimal and clean **HTML/CSS frontend**

---

## Tech Stack

| Layer           | Technology            |
| --------------- | --------------------- |
| Frontend        | HTML, CSS, JavaScript |
| Backend         | Python + FastAPI      |
| Vector Database | FAISS                 |
| Embeddings      | Sentence Transformers |
| File Parsing    | PyPDF                 |

---

## Project Structure

```
ragdb/
│
├── backend/
│   ├── app.py
│   ├── rag.py
│   ├── requirements.txt
│   ├── uploads/
│   └── vector_store/
│
└── frontend/
    ├── index.html
    ├── style.css
    └── script.js
```

---

## Installation

### 1️⃣ Clone the Repository

```
git clone https://github.com/yourusername/ragdb.git
cd ragdb
```

---

### 2️⃣ Setup Backend

```
cd backend
```

Create virtual environment

```
python -m venv venv
```

Activate environment

**Mac / Linux**

```
source venv/bin/activate
```

**Windows**

```
venv\Scripts\activate
```

Install dependencies

```
pip install -r requirements.txt
```

Start backend server

```
uvicorn app:app --reload
```

Backend will run at:

```
http://127.0.0.1:8000
```

---

### 3️⃣ Run Frontend

Open a new terminal:

```
cd frontend
```

Run simple server

```
python -m http.server 5500
```

Open browser

```
http://localhost:5500
```

---

## How RagDB Works

```
User Uploads PDF
        ↓
Text Extraction
        ↓
Text Chunking
        ↓
Embedding Generation
        ↓
Vector Storage (FAISS)
        ↓
User Query
        ↓
Similarity Search
        ↓
Retrieve Best Chunks
        ↓
Return Brief Answer
```

---

## Example Workflow

1. Upload a PDF document
2. RagDB extracts and chunks the text
3. Chunks are converted into embeddings
4. Embeddings are stored in the vector database
5. User asks a question
6. RagDB retrieves the most relevant sections
7. A brief answer is generated from the retrieved context

---

## Future Improvements

* Multi-document search
* Chat-style interface
* Citation support
* LLM-based summarization
* DOCX and TXT support
* Authentication for multi-user systems
* Docker deployment

---

## License

MIT License
