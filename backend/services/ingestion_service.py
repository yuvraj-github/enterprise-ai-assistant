import uuid

from services.chroma_service import add_documents


CHUNK_SIZE = 1000
CHUNK_OVERLAP = 150


def _split_into_chunks(text: str) -> list[str]:
    normalized_text = " ".join(text.split())
    if not normalized_text:
        return []

    chunks = []
    step = CHUNK_SIZE - CHUNK_OVERLAP

    for start in range(0, len(normalized_text), step):
        chunk = normalized_text[start : start + CHUNK_SIZE].strip()
        if chunk:
            chunks.append(chunk)

    return chunks


def ingest_document(
    pages: list[tuple[int, str]],
    filename: str,
    document_hash: str,
    department: str = "General",
) -> dict:
    document_id = str(uuid.uuid4())
    title = filename.rsplit(".", 1)[0]
    documents = []
    ids = []
    metadatas = []

    for page_number, page_text in pages:
        for chunk_number, chunk in enumerate(_split_into_chunks(page_text), start=1):
            documents.append(chunk)
            ids.append(
                f"{document_id}_page_{page_number}_chunk_{chunk_number}"
            )
            metadatas.append(
                {
                    "title": title,
                    "page": page_number,
                    "department": department,
                    "document_id": document_id,
                    "document_hash": document_hash,
                    "filename": filename,
                }
            )

    if not documents:
        raise ValueError("The document contains no extractable text.")

    add_documents(documents, ids, metadatas)

    return {
        "document_id": document_id,
        "chunks_added": len(documents),
    }
