from pathlib import Path

import chromadb


CHROMA_DB_PATH = Path(__file__).resolve().parents[1] / "chroma_db"
chroma = chromadb.PersistentClient(path=str(CHROMA_DB_PATH))
collection = chroma.get_or_create_collection(name="company_policies")


def add_documents(
    documents: list[str],
    ids: list[str],
    metadatas: list[dict],
) -> None:
    collection.upsert(
        documents=documents,
        ids=ids,
        metadatas=metadatas,
    )


def document_hash_exists(document_hash: str) -> bool:
    result = collection.get(
        where={"document_hash": document_hash},
        limit=1,
    )
    return bool(result["ids"])

def delete_document_by_filename(filename: str) -> None:
    collection.delete(
        where={"filename": filename}
    )


def search_documents(question: str, n_results: int = 3) -> dict:
    return collection.query(
        query_texts=[question],
        n_results=n_results,
    )
