from app.retriever import retrieve_top_10
from app.reranker import rerank_documents
from app.prompts import build_prompt
from app.llm import generate_answer


question = "What is the attendance requirement?"


print("================================")
print("1. RETRIEVING TOP 10")
print("================================")


top_10 = retrieve_top_10(
    question
)


for index, chunk in enumerate(top_10):

    print(
        f"{index + 1}. "
        f"Page {chunk['page']} "
        f"Score {chunk['score']:.4f}"
    )


print("\n================================")
print("2. RERANKING")
print("================================")


top_3 = rerank_documents(
    question,
    top_10,
    top_n=3
)


for index, chunk in enumerate(top_3):

    print(
        f"{index + 1}. "
        f"Page {chunk['page']} "
        f"Rerank Score "
        f"{chunk['rerank_score']:.4f}"
    )


print("\n================================")
print("3. PROMPT")
print("================================")


prompt = build_prompt(
    question,
    top_3
)

print(prompt)


print("\n================================")
print("4. LLM ANSWER")
print("================================")


answer = generate_answer(
    prompt
)

print(answer)