from app.pdf_processor import (
    extract_text_from_pdf,
    create_chunks
)

from app.embeddings import get_embeddings

from app.vector_store import (
    create_collection,
    insert_chunks
)


PDF_PATH = "data/Tourism.pdf"


print("================================")
print("STEP 1: PDF EXTRACTION")
print("================================")

pages = extract_text_from_pdf(
    PDF_PATH
)

print(
    "Pages extracted:",
    len(pages)
)


print("\n================================")
print("STEP 2: CHUNKING")
print("================================")

chunks = create_chunks(
    pages,
    chunk_size=1000,
    overlap=200
)

print(
    "Chunks created:",
    len(chunks)
)


print("\n================================")
print("STEP 3: EMBEDDINGS")
print("================================")

texts = [
    chunk["text"]
    for chunk in chunks
]

embeddings = get_embeddings(
    texts
)

print(
    "Embeddings generated:",
    len(embeddings)
)


vector_size = len(
    embeddings[0]
)

print(
    "Vector size:",
    vector_size
)


print("\n================================")
print("STEP 4: QDRANT COLLECTION")
print("================================")

create_collection(
    vector_size
)

print(
    "Qdrant collection created."
)


print("\n================================")
print("STEP 5: INSERTING VECTORS")
print("================================")

insert_chunks(
    chunks,
    embeddings
)

print(
    "Vectors inserted:",
    len(chunks)
)


print("\n================================")
print("INDEXING COMPLETE")
print("================================")