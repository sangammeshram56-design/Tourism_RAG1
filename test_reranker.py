""" from app.retriever import retrieve_top_10
from app.reranker import rerank_documents


question = "What is the attendance requirement?"


print("================================")
print("STEP 1: RETRIEVAL")
print("================================")

top_10 = retrieve_top_10(
    question
)


for index, chunk in enumerate(top_10):

    print(
        index + 1,
        "| Page:",
        chunk["page"],
        "| Score:",
        round(
            chunk["score"],
            4
        )
    )


print("\n================================")
print("STEP 2: RERANKING")
print("================================")


top_3 = rerank_documents(
    question,
    top_10,
    top_n=3
)


print("\n================================")
print("TOP 3 AFTER RERANKING")
print("================================")


for index, chunk in enumerate(top_3):

    print("\n----------------------------")

    print(
        "Rank:",
        index + 1
    )

    print(
        "Page:",
        chunk["page"]
    )

    print(
        "Retrieval score:",
        round(
            chunk["retrieval_score"],
            4
        )
    )

    print(
        "Rerank score:",
        round(
            chunk["rerank_score"],
            4
        )
    )

    print(
        "Text:",
        chunk["text"][:500]
    ) 
    
    """








from app.retriever import retrieve_top_10
from app.reranker import rerank_documents


# ==================================================
# USER QUESTION
# ==================================================

question = "What are the major types of tourism in Maharashtra?"


# ==================================================
# STEP 1: RETRIEVE TOP 10 FROM QDRANT
# ==================================================

print("================================")
print("STEP 1: RETRIEVAL")
print("================================")

top_10 = retrieve_top_10(question)


for index, chunk in enumerate(top_10):

    print(
        index + 1,
        "| Page:",
        chunk["page"],
        "| Qdrant Score:",
        round(chunk["score"], 4)
    )


# ==================================================
# STEP 2: RERANK TOP 10
# USING SENTENCE TRANSFORMER
# ==================================================

print("\n================================")
print("STEP 2: SENTENCE TRANSFORMER RERANKING")
print("================================")

top_5 = rerank_documents(
    question,
    top_10,
    top_n=5
)


# ==================================================
# STEP 3: DISPLAY TOP 5
# ==================================================

print("\n================================")
print("TOP 5 AFTER RERANKING")
print("================================")


for index, chunk in enumerate(top_5):

    print("\n----------------------------")

    print(
        "Rank:",
        index + 1
    )

    print(
        "Page:",
        chunk["page"]
    )

    print(
        "Qdrant retrieval score:",
        round(
            chunk["retrieval_score"],
            4
        )
    )

    print(
        "SentenceTransformer cosine score:",
        round(
            chunk["rerank_score"],
            4
        )
    )

    print("Text:")

    print(
        chunk["text"][:500]
    )