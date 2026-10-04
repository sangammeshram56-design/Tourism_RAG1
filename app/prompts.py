def build_prompt(
    question,
    chunks
):

    context_parts = []

    for index, chunk in enumerate(chunks):

        context_parts.append(
            f"""
Context {index + 1}
Source: {chunk["source"]}
Page: {chunk["page"]}

Content:
{chunk["text"]}
"""
        )

    context = "\n".join(
        context_parts
    )

    prompt = f"""
You are a document question-answering assistant.

Answer the user's question using ONLY
the information provided in the context.

Do not use outside knowledge.

If the answer is not available in the
provided context, say:

"The information is not available
in the provided document."

Context:
{context}

Question:
{question}

Answer:
"""

    return prompt