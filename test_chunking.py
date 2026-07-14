from src.document_loader import load_documents
from src.chunker import chunk_document

documents = load_documents("documents")

all_chunks = []

for document in documents:
    chunks = chunk_document(document)

    all_chunks.extend(chunks)

for chunk in all_chunks[:10]:

    print("\n")
    print("=" * 80)

    print(chunk["source"])

    print("-" * 80)

    print(chunk["text"][:500])

print(f"\nTotal Chunks: {len(all_chunks)}\n")

print("=" * 60)

print(all_chunks[0]["source"])

print("=" * 60)

print(all_chunks[0]["text"])