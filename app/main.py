from fastapi import FastAPI
from pydantic import BaseModel
from app.retriever import retrieve_top_10
from app.reranker import rerank_documents
from app.prompts import build_prompt
from app.llm import generate_answer
from app.pdf_processor import extract_text_from_pdf 

app =  FastAPI(
    title="Mini RAG Application",
    description="PDF Question Answering using RAG",
    version="1.0.0"
)


class QuestionRequest(BaseModel):

    question: str


@app.get("/")
def root():

    return {
        "message": "Mini RAG API is running"
    }


@app.post("/ask")
def ask_question(
    request: QuestionRequest
):

    question = request.question

    top_10 = retrieve_top_10(
        question
    )

    top_3 = rerank_documents(
        question,
        top_10,
        top_n=3
    )

    prompt = build_prompt(
        question,
        top_3
    )

    answer = generate_answer(
        prompt
    )

    return {
        "question": question,
        "answer": answer,
        "retrieved_chunks": top_10,
        "reranked_chunks": top_3
    }