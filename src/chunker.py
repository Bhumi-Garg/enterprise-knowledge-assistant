def chunk_text(text, chunk_size=500, overlap=50):
    chunks = []

    start = 0

    while start < len(text):
        end = start + chunk_size

        chunk = text[start:end]

        chunks.append(chunk)

        start += chunk_size - overlap

    return chunks


def chunk_document(document):
    chunks = chunk_text(document["text"])

    chunk_objects = []

    for idx, chunk in enumerate(chunks):
        chunk_objects.append(
            {
                "chunk_id": f"{document['filename']}_{idx}",
                "source": document["filename"],
                "text": chunk
            }
        )

    return chunk_objects