from src.document_loader import load_documents
from src.chunker import chunk_document

documents = load_documents("documents")

all_chunks = []

for document in documents:
    chunks = chunk_document(document)

    all_chunks.extend(chunks)

print(f"\nTotal Chunks: {len(all_chunks)}\n")

print("=" * 60)

print(all_chunks[0]["source"])

print("=" * 60)

print(all_chunks[0]["text"])