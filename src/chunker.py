def chunk_text(text, chunk_size=1200):
    
    paragraphs = text.split("\n\n")

    chunks = []

    current_chunk = ""

    for paragraph in paragraphs:

        paragraph = paragraph.strip()

        if not paragraph:
            continue

        if len(current_chunk) + len(paragraph) < chunk_size:

            current_chunk += paragraph + "\n\n"

        else:

            chunks.append(current_chunk.strip())

            current_chunk = paragraph + "\n\n"

    if current_chunk:
        chunks.append(current_chunk.strip())

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