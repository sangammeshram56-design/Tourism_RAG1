from app.query_enhancer import enhance_query


question = input("Enter your question: ").strip()

enhanced_query = enhance_query(question)

print()
print("Original question:")
print(question)

print()
print("Enhanced query:")
print(enhanced_query)