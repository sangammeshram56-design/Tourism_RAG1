from app.pdf_processor import extract_text_from_pdf


pdf_path = "data/Tourism.pdf"

pages = extract_text_from_pdf(pdf_path)

print("Number of pages:", len(pages))

for page in pages[:2]:
    print("\n-------------------------")
    print("Page:", page["page"])
    print("Source:", page["source"])
    print("Text:")
    print(page["text"][:100])  # Print first 100 characters of text
