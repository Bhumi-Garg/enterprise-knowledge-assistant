def chunk_text(text, chunk_size=1200, overlap=200):

    chunks = []

    start = 0

    while start < len(text):

        end = start + chunk_size

        chunk = text[start:end]

        if chunk.strip():
            chunks.append(chunk.strip())

        start += (
            chunk_size - overlap
        )

    return chunks


def chunk_document(document):
    chunks = chunk_text(document["text"])

    chunk_objects = []

    for idx, chunk in enumerate(chunks):
        chunk_objects.append(
            {
                "chunk_id": f"{document['filename']}_{idx}",
                "source": document["filename"],
                "category": get_category(document["filename"]),
                "text": chunk
            }
        )

    return chunk_objects

def get_category(filename):
    filename = filename.lower()

    if "leave" in filename or "handbook" in filename:
        return "HR"

    if "expense" in filename:
        return "Finance"

    if "vpn" in filename:
        return "Security"

    if "incident" in filename:
        return "Operations"

    if "product" in filename:
        return "Product"

    return "General"