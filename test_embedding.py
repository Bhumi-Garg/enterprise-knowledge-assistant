from src.document_loader import load_documents
from src.chunker import chunk_document
from src.embedder import generate_embeddings

documents = load_documents("documents")

all_chunks = []

for document in documents:
    all_chunks.extend(
        chunk_document(document)
    )

embeddings = generate_embeddings(all_chunks)

print("Total chunks:", len(all_chunks))

print("Embedding shape:")
print(embeddings.shape)

print("First vector length:")
print(len(embeddings[0]))