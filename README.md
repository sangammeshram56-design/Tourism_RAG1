# Tourism RAG – Tourism Information Assistant

A Retrieval-Augmented Generation (RAG) based Tourism Information Assistant that provides relevant and context-aware information about tourist destinations using a tourism knowledge base.

---

### RAG Workflow

```text
                    USER
                      │
                      ▼
               User Question
                      │
                      ▼
             Query Embedding
                      │
                      ▼
              Vector Search
                      │
                      ▼
             Qdrant Database
                      │
                      ▼
            Retrieved Documents
                      │
                      ▼
                  Reranker
                      │
                      ▼
             Relevant Context
                      │
                      ▼
                    LLM
                      │
                      ▼
              Generated Answer
                      │
                      ▼
                    USER
```

---
# 📋 Complete RAG Pipeline

The complete project workflow can be summarized as:

```text
                    DOCUMENT INGESTION
                           │
                           ▼
                  ┌─────────────────┐
                  │ Tourism Files   │
                  └────────┬────────┘
                           │
                           ▼
                  ┌─────────────────┐
                  │ Text Extraction │
                  └────────┬────────┘
                           │
                           ▼
                  ┌─────────────────┐
                  │    Chunking     │
                  └────────┬────────┘
                           │
                           ▼
                  ┌─────────────────┐
                  │   Embeddings    │
                  └────────┬────────┘
                           │
                           ▼
                  ┌─────────────────┐
                  │ Qdrant Database │
                  └─────────────────┘


                    QUERY PROCESSING
                           │
                           ▼
                  ┌─────────────────┐
                  │   User Query    │
                  └────────┬────────┘
                           │
                           ▼
                  ┌─────────────────┐
                  │ Query Embedding │
                  └────────┬────────┘
                           │
                           ▼
                  ┌─────────────────┐
                  │ Qdrant Search   │
                  └────────┬────────┘
                           │
                           ▼
                  ┌─────────────────┐
                  │  Top 10 Results │
                  └────────┬────────┘
                           │
                           ▼
                  ┌─────────────────┐
                  │    Reranker     │
                  └────────┬────────┘
                           │
                           ▼
                  ┌─────────────────┐
                  │  Top 3 Results  │
                  └────────┬────────┘
                           │
                           ▼
                  ┌─────────────────┐
                  │ Relevant Context│
                  └────────┬────────┘
                           │
                           ▼
                  ┌─────────────────┐
                  │      LLM        │
                  └────────┬────────┘
                           │
                           ▼
                  ┌─────────────────┐
                  │ Final Response  │
                  └─────────────────┘
```

---

# 📦 Installation

## Step 1 – Clone the Repository

```bash
git clone https://github.com/sangammeshram56-design/Tourism_RAG.git
```

Move into the project directory:

```bash
cd Tourism_RAG
```

---

## Step 2 – Create a Virtual Environment

For Windows:

```bash
python -m venv venv
```

---

## Step 3 – Activate the Virtual Environment

For PowerShell:

```powershell
venv\Scripts\Activate.ps1
```

For Command Prompt:

```cmd
venv\Scripts\activate
```

After activation, the terminal should show something similar to:

```text
(venv)
```

---

## Step 4 – Install Dependencies

Install the required Python packages:

```bash
pip install -r requirements.txt
```

---

# ▶️ Running the Project

After installing the dependencies and configuring the environment, start the FastAPI application.

```bash
uvicorn app.main:app --reload
```

The application will start on the local server.

By default:

```text
http://127.0.0.1:8000
```

---

# 📖 API Documentation

FastAPI automatically provides interactive API documentation.

After starting the application, open:

```text
http://127.0.0.1:8000/docs
```

The Swagger interface 

---


# 📂 Project Structure

The project is organized into separate modules so that each component has a specific responsibility.

```text
Tourism_RAG/
│
├── app/
│   ├── __init__.py
│   ├── config.py
│   ├── embeddings.py
│   ├── llm.py
│   ├── main.py
│   ├── pdf_processor.py
│   ├── prompts.py
│   ├── reranker.py
│   ├── retriever.py
│   └── vector_store.py
│
├── data/
│   └── Tourism Documents
│
├── screenshots/
│   └── Project Screenshots
│
├── qdrant_data/
│   └── Local Qdrant Database
│
├── add.py
├── requirements.txt
├── .env
├── .gitignore
└── README.md
```

---

# 🛠️ Technologies Used

| Technology      | Purpose                         |
| --------------- | ------------------------------- |
| Python          | Main programming language       |
| FastAPI         | Backend API framework           |
| Uvicorn         | ASGI server                     |
| Qdrant          | Vector database                 |
| Embedding Model | Converts text into vectors      |
| Reranker Model  | Ranks retrieved documents       |
| LLM             | Generates final responses       |
| PyMuPDF         | PDF text extraction             |
| Requests        | API communication               |
| python-dotenv   | Environment variable management |

---

# 💬 Example Queries

The Tourism RAG system can be used for questions such as:

```text
1. What are the best places to visit in Goa?

2. What are the popular tourist attractions in Rajasthan?

3. What is the best time to visit Kerala?

The response depends on the information available in the project's knowledge base.

---
