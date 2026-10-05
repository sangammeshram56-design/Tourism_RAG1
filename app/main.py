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


# =========================
# REQUEST MODEL
# =========================

class QuestionRequest(BaseModel):
    question: str


# =========================
# TOP 3 CHUNK MODEL
# =========================

class RetrievedChunk(BaseModel):
    rank: int
    page: int
    source: str
    score: float
    text: str


# =========================
# RESPONSE MODEL
# =========================

class QueryResponse(BaseModel):
    question: str
    answer: str
    reranked_chunks: list[RetrievedChunk]


# =========================
# ROOT
# =========================

@app.get("/")
def root():
    return {
        "message": "Tourism Maharashtra RAG API is running"
    }


# =========================
# ASK QUESTION
# =========================

@app.post(
    "/ask",
    response_model=QueryResponse
)
def ask_question(request: QuestionRequest):

    # Original question
    question = request.question

    # --------------------------------
    # STEP 1: QUERY ENHANCEMENT
    # --------------------------------

    enhanced_query = enhance_query(question)

    # --------------------------------
    # STEP 2: RETRIEVE TOP 10
    # --------------------------------
    # Top 10 are used internally only

    top_10 = retrieve_top_10(
        enhanced_query
    )

    # --------------------------------
    # STEP 3: RERANK TOP 10 → TOP 3
    # --------------------------------

    top_3 = rerank_documents(
        enhanced_query,
        top_10,
        top_n=3
    )

    # --------------------------------
    # STEP 4: BUILD PROMPT
    # --------------------------------

    prompt = build_prompt(
        question,
        top_3
    )

    # --------------------------------
    # STEP 5: GENERATE ANSWER
    # --------------------------------

    answer = generate_answer(prompt)

    # --------------------------------
    # STEP 6: PREPARE ONLY TOP 3
    # --------------------------------

    final_chunks = []

    for index, chunk in enumerate(top_3):

        final_chunks.append(
            RetrievedChunk(
                rank=index + 1,
                page=chunk["page"],
                source=chunk["source"],
                score=chunk["retrieval_score"],
                text=chunk["text"]
            )
        )

    # --------------------------------
    # FINAL RESPONSE
    # --------------------------------

    return QueryResponse(
        question=question,
        answer=answer,
        reranked_chunks=final_chunks
    )