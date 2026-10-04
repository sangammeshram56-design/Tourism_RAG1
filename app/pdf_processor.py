""" import pymupdf
import os


def extract_text_from_pdf(pdf_path):
    
    Extract text from a PDF file using PyMuPDF.
    Returns a list of dictionaries containing
    source, page number, and extracted text.
    

    # Check if PDF exists
    if not os.path.exists(pdf_path):
        print(f"ERROR: PDF not found at: {pdf_path}")
        return []

    print(f"Opening PDF: {pdf_path}")

    # Open PDF
    document = pymupdf.open(pdf_path)

    pages = []

    # Extract text from each page
    for page_number, page in enumerate(document):

        text = page.get_text()

        if text.strip():
            pages.append({
                "source": pdf_path,
                "page": page_number + 1,
                "text": text.strip()
            })

            print(f"Extracted text from page {page_number + 1}")

        else:
            print(f"No text found on page {page_number + 1}")

    # Close PDF
    document.close()

    print(f"\nTotal pages with text: {len(pages)}")

    return pages


# =========================================================
# MAIN PROGRAM
# =========================================================

if __name__ == "__main__":

    # Path to your PDF
    pdf_path = "data/Tourism.pdf"

    # Extract text
    pages = extract_text_from_pdf(pdf_path)

    # Display extracted text
    if pages:

        print("\n" + "=" * 10)
        print("EXTRACTED PDF TEXT")
        print("=" * 10)

        for page in pages:
            print(f"\n--- Page {page['page']} ---")
            print(page["text"])

    else:
        print("\nNo text was extracted from the PDF.")

 """
""" import pymupdf


pdf_path = "data/Tourism.pdf"
def extract_text_from_pdf(pdf_path):
    Extract text from a PDF file using PyMuPDF.
    document = pymupdf.open(pdf_path)

    pages = []

    for page_number, page in enumerate(document):
        text = page.get_text()

        if text.strip():
            pages.append({
                "source": pdf_path,
                "page": page_number + 1,
                "text": text.strip()
            })

    document.close()

    return pages


def create_chunks(pages, chunk_size=1000, overlap=200):
    chunks = []

    for page in pages:
        text = page["text"]
        start = 0

        while start < len(text):
            end = start + chunk_size
            chunk_text = text[start:end]

            if chunk_text.strip():
                chunks.append({
                    "text": chunk_text.strip(),
                    "source": page["source"],
                    "page": page["page"]
                })

            start += chunk_size - overlap

    return chunks
 """



import pymupdf


# ---------------------------------------------------------
# Configuration
# ---------------------------------------------------------

PDF_PATH = "data/Tourism.pdf"

CHUNK_SIZE = 1000
CHUNK_OVERLAP = 200


# ---------------------------------------------------------
# 1. Extract text from PDF
# ---------------------------------------------------------

def extract_text_from_pdf(pdf_path):
    """
    Extract text from each page of a PDF using PyMuPDF.

    Returns:
        List of dictionaries containing:
        - source
        - page
        - text
    """

    document = pymupdf.open(pdf_path)

    pages = []

    for page_number, page in enumerate(document):
        text = page.get_text()

        if text.strip():
            pages.append({
                "source": pdf_path,
                "page": page_number + 1,
                "text": text.strip()
            })

    document.close()

    return pages


# ---------------------------------------------------------
# 2. Create chunks
# ---------------------------------------------------------

def create_chunks(pages, chunk_size=1000, overlap=200):
    """
    Split page text into overlapping chunks.

    Example:
        chunk_size = 1000
        overlap = 200

    Chunk 1: characters 0-999
    Chunk 2: characters 800-1799
    Chunk 3: characters 1600-2599
    """

    if overlap >= chunk_size:
        raise ValueError(
            "overlap must be smaller than chunk_size"
        )

    chunks = []

    step = chunk_size - overlap

    for page in pages:

        text = page["text"]

        start = 0

        while start < len(text):

            end = start + chunk_size

            chunk_text = text[start:end].strip()

            if chunk_text:

                chunks.append({
                    "text": chunk_text,
                    "source": page["source"],
                    "page": page["page"]
                })

            start += step

    return chunks


# ---------------------------------------------------------
# 3. Print extracted pages
# ---------------------------------------------------------

def print_pages(pages):

    print("\n")
    print("=" * 80)
    print("EXTRACTED PAGES")
    print("=" * 80)

    print(f"Number of pages: {len(pages)}")

    for page in pages:

        print("\n" + "-" * 80)
        print(f"Page: {page['page']}")
        print(f"Source: {page['source']}")
        print("Text:")
        print(page["text"])


# ---------------------------------------------------------
# 4. Print chunks
# ---------------------------------------------------------

def print_chunks(chunks):

    print("\n")
    print("=" * 80)
    print("CREATED CHUNKS")
    print("=" * 80)

    print(f"Number of chunks: {len(chunks)}")
    print(f"Chunk size: {CHUNK_SIZE}")
    print(f"Overlap: {CHUNK_OVERLAP}")

    for i, chunk in enumerate(chunks, start=1):

        print("\n" + "-" * 80)

        print(f"Chunk: {i}")
        print(f"Page: {chunk['page']}")
        print(f"Source: {chunk['source']}")
        print(f"Characters: {len(chunk['text'])}")

        print("\nText:")
        print(chunk["text"])


# ---------------------------------------------------------
# 5. Main
# ---------------------------------------------------------

def main():

    print("=" * 80)
    print("PDF PROCESSOR")
    print("=" * 80)

    print(f"PDF: {PDF_PATH}")
    print(f"Chunk size: {CHUNK_SIZE}")
    print(f"Chunk overlap: {CHUNK_OVERLAP}")

    # Extract PDF text
    pages = extract_text_from_pdf(PDF_PATH)

    # Check if PDF contains text
    if not pages:
        print("\nNo text found in the PDF.")
        return

    # Print extracted pages
    print_pages(pages)

    # Create chunks
    chunks = create_chunks(
        pages,
        chunk_size=CHUNK_SIZE,
        overlap=CHUNK_OVERLAP
    )

    # Print chunks
    print_chunks(chunks)


# ---------------------------------------------------------
# Run program
# ---------------------------------------------------------

if __name__ == "__main__":
    main()