from fastapi import FastAPI
from pydantic import BaseModel

from app.query_enhancer import enhance_query
from app.retriever import retrieve_top_10
from app.reranker import rerank_documents
from app.prompts import build_prompt
from app.llm import generate_answer


app = FastAPI(
    title="Tourism Maharashtra RAG",
    description="Question Answering using Tourism.pdf",
    version="1.0.0"
)


class QuestionRequest(BaseModel):
    question: str


class QueryResponse(BaseModel):
    question: str
    answer: str


@app.get("/")
def root():
    return {
        "message": "Tourism Maharashtra RAG API is running"
    }


@app.post(
    "/ask",
    response_model=QueryResponse
)
def ask_question(request: QuestionRequest):

    # Original user question
    question = request.question

    # Step 1: Query enhancement
    enhanced_query = enhance_query(question)

    # Step 2: Retrieve Top 10
    top_10 = retrieve_top_10(enhanced_query)

    # Step 3: Rerank Top 10 → Top 3
    top_3 = rerank_documents(
        enhanced_query,
        top_10,
        top_n=3
    )

    # Step 4: Build prompt
    prompt = build_prompt(
        question,
        top_3
    )

    # Step 5: Generate final answer
    answer = generate_answer(prompt)

    # Only question and answer are returned
    return QueryResponse(
        question=question,
        answer=answer
    )