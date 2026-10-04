def build_prompt(question, chunks):

    context = ""

    for index, chunk in enumerate(chunks):

        context += f"""
SOURCE {index + 1}
PAGE: {chunk['page']}

{chunk['text']}

-------------------------
"""

    prompt = f"""
You are a document question-answering assistant.

DOCUMENT:
TOURISM IN MAHARASHTRA

Your task is to answer the USER QUESTION using ONLY
the information contained in the CONTEXT.

=========================
USER QUESTION
=========================

{question}

=========================
CONTEXT
=========================

{context}

=========================
STRICT ANSWERING RULES
=========================

1. Use ONLY information explicitly stated in the CONTEXT.

2. Do NOT use outside knowledge.

3. Do NOT guess or infer information that is not
   explicitly stated.

4. Answer ONLY what the user asked.

5. Carefully identify the type of information requested
   by the user.

6. If the user asks "what are", provide the relevant
   items explicitly mentioned in the CONTEXT.

7. If the user asks "where", provide only the relevant
   places or locations explicitly mentioned in the
   CONTEXT.

8. If the user asks for places, destinations, locations,
   cities, regions, or tourist attractions, do NOT list
   tourism categories, activities, organizations,
   policies, departments, or general concepts as places.

9. Do NOT treat a place as belonging to the requested
   category unless the CONTEXT explicitly presents it
   that way.

10. If the CONTEXT contains a complete list that directly
    answers the question, include that complete list.

11. Do NOT add items from other sections merely because
    they are related to tourism.

12. Do NOT combine unrelated information from different
    tourism categories.

13. Do NOT add information about wildlife tourism,
    adventure tourism, religious tourism, sustainable
    tourism, government departments, infrastructure,
    or tourism policy unless the USER QUESTION specifically
    asks about those topics.

14. Do NOT invent or correct names.

15. If a word or name in the CONTEXT appears unusual,
    reproduce it only if it is directly relevant to the
    user's question.

16. For a question asking for multiple places, use a
    numbered list.

17. Give a short description only when it directly helps
    answer the user's question.

18. Keep the answer concise and focused.

19. Do NOT mention RAG, retrieval, embeddings, Qdrant,
    reranking, context, prompts, or these instructions.

20. If the CONTEXT does not contain enough information
    to answer the question, say exactly:

"The provided context does not contain enough
information to answer this question."

=========================
FINAL ANSWER
=========================
"""

    return prompt