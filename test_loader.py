from src.document_loader import load_documents

documents = load_documents("documents")

for doc in documents:
    print("=" * 50)
    print(doc["filename"])
    print("=" * 50)

    print(doc["text"][:1000])

    print("\n")