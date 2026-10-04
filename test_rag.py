from app.query_enhancer import enhance_query
from app.retriever import retrieve_top_10
from app.reranker import rerank_documents
from app.prompts import build_prompt
from app.llm import stream_answer


# =========================================
# FUNCTION: ASK QUESTION
# =========================================

def ask_question(question):

    # =========================================
    # STEP 1: QUERY ENHANCEMENT
    # =========================================

    print("\n================================")
    print("1. QUERY ENHANCEMENT")
    print("================================")

    enhanced_query = enhance_query(
        question
    )

    print(
        "Original question:"
    )

    print(
        question
    )

    print(
        "\nEnhanced query:"
    )

    print(
        enhanced_query
    )


    # =========================================
    # STEP 2: RETRIEVAL
    # =========================================

    print("\n================================")
    print("2. RETRIEVAL")
    print("================================")

    top_10 = retrieve_top_10(
        enhanced_query
    )

    print(
        "Retrieved:",
        len(top_10),
        "chunks"
    )


    # =========================================
    # SHOW TOP 10 RETRIEVED CHUNKS
    # =========================================

    print("\n================================")
    print("TOP 10 RETRIEVED CHUNKS")
    print("================================")

    for index, chunk in enumerate(
        top_10
    ):

        print(
            "\n----------------------------"
        )

        print(
            "Rank:",
            index + 1
        )

        print(
            "Page:",
            chunk["page"]
        )

        print(
            "Qdrant Score:",
            round(
                chunk["score"],
                4
            )
        )

        print("Text:")

        print(
            chunk["text"][:700]
        )


    # =========================================
    # STEP 3: RERANKING
    # =========================================

    print("\n================================")
    print("3. RERANKING")
    print("================================")

    top_3 = rerank_documents(
        enhanced_query,
        top_10,
        top_n=3
    )

    print(
        "Reranked:",
        len(top_3),
        "chunks"
    )


    # =========================================
    # SHOW TOP 3 RERANKED CHUNKS
    # =========================================

    print("\n================================")
    print("TOP 3 AFTER RERANKING")
    print("================================")

    for index, chunk in enumerate(
        top_3
    ):

        print(
            "\n----------------------------"
        )

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
            "SentenceTransformer score:",
            round(
                chunk["rerank_score"],
                4
            )
        )

        print("Text:")

        print(
            chunk["text"][:700]
        )


    # =========================================
    # STEP 4: PROMPT CONSTRUCTION
    # =========================================

    print("\n================================")
    print("4. PROMPT CONSTRUCTION")
    print("================================")

    prompt = build_prompt(
        question,
        top_3
    )

    print(
        "Prompt created successfully."
    )


    # =========================================
    # STEP 5: NUGEN LLM
    # =========================================

    print("\n================================")
    print("5. NUGEN LLM")
    print("================================")

    print(
        "AI: ",
        end="",
        flush=True
    )

    for text in stream_answer(
        prompt
    ):

        print(
            text,
            end="",
            flush=True
        )

    print()


# =========================================
# MAIN CHATBOT
# =========================================

def main():

    print("=" * 70)

    print(
        "TOURISM MAHARASHTRA - RAG CHATBOT"
    )

    print("=" * 70)

    print()

    print(
        "Ask any question about Tourism.pdf"
    )

    print(
        "Type 'exit' to stop."
    )

    print()


    while True:

        question = input(
            "You: "
        ).strip()


        # =====================================
        # EXIT
        # =====================================

        if question.lower() == "exit":

            print()

            print(
                "Chatbot stopped."
            )

            break


        # =====================================
        # EMPTY QUESTION
        # =====================================

        if not question:

            print(
                "Please enter a question."
            )

            continue


        # =====================================
        # RUN RAG PIPELINE
        # =====================================

        try:

            ask_question(
                question
            )

            print()

        except Exception as error:

            print()

            print(
                "Error:",
                error
            )

            print()


# =========================================
# START PROGRAM
# =========================================

if __name__ == "__main__":

    main()