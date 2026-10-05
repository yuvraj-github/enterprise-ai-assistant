from services.chroma_service import search_documents
from services.claude_service import generate_answer


MAX_DISTANCE = 1.10


def ask_rag(question: str):

    # Step 1: Search Chroma
    results = search_documents(question)

    documents = results["documents"][0]
    metadatas = results["metadatas"][0]
    distances = results["distances"][0]

    # Step 2: Keep only relevant documents
    relevant_documents = []
    relevant_metadatas = []

    for document, metadata, distance in zip(
        documents,
        metadatas,
        distances
    ):
        print("\nDOCUMENT:")
        print(document)
    
        print("METADATA:")
        print(metadata)
    
        print("DISTANCE:")
        print(distance)

        print("===============================\n")

        if distance <= MAX_DISTANCE:
            relevant_documents.append(document)
            relevant_metadatas.append(metadata)

    # Step 3: Nothing relevant found
    if not relevant_documents:
        return {
            "answer": "I don't know based on the provided information.",
            "sources": []
        }

    # Step 4: Build context
    context = "\n\n".join(relevant_documents)

    # Step 5: Build grounded prompt
    prompt = f"""
You are an enterprise HR assistant.

Answer the question using only the provided context.

If the answer is not available in the context,
say "I don't know based on the provided information."

Context:
{context}

Question:
{question}
"""

    # Step 6: Ask Claude
    answer = generate_answer(prompt)

    # Step 7: Build citations
    sources = []
    seen_citations = set()

    for metadata in relevant_metadatas:
        citation_key = (
            metadata["title"],
            metadata["page"],
            metadata["department"],
        )
        if citation_key in seen_citations:
            continue

        seen_citations.add(citation_key)
        source = {
            "title": metadata["title"],
            "page": metadata["page"],
            "department": metadata["department"]
        }

        sources.append(source)

    return {
        "answer": answer,
        "sources": sources
    }