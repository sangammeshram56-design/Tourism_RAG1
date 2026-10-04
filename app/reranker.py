import requests

from app.config import (
    NUGEN_API_KEY,
    NUGEN_RERANKER_MODEL
)


NUGEN_RERANK_URL = (
    "https://api.nugen.in/api/v3/inference/reranker"
)


def rerank_documents(
    question,
    chunks,
    top_n=3
):

    documents = [
        chunk["text"]
        for chunk in chunks
    ]

    headers = {
        "Authorization": f"Bearer {NUGEN_API_KEY}",
        "Content-Type": "application/json"
    }

    payload = {
        "model": NUGEN_RERANKER_MODEL,
        "query": question,
        "documents": documents,
        "method": "fast",
        "top_n": top_n,
        "return_documents": True
    }

    response = requests.post(
        NUGEN_RERANK_URL,
        headers=headers,
        json=payload,
        timeout=120
    )

    response.raise_for_status()

    data = response.json()

    reranked_chunks = []

    for result in data["results"]:

        original_index = result["index"]

        original_chunk = chunks[
            original_index
        ]

        reranked_chunks.append({
            "text": original_chunk["text"],
            "source": original_chunk["source"],
            "page": original_chunk["page"],
            "chunk_id": original_chunk["chunk_id"],
            "retrieval_score": original_chunk["score"],
            "rerank_score": result[
                "relevance_score"
            ]
        })

    return reranked_chunks