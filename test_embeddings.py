from app.embeddings import get_embedding


text = "Students must maintain the required attendance percentage."

vector = get_embedding(text)

print("Embedding generated successfully.")

print("Vector size:", len(vector))

print("First 10 values:")

print(vector[:10])