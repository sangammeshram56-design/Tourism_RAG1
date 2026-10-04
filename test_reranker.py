from app.retriever import retrieve_top_10
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