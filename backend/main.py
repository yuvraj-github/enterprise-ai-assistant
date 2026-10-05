import hashlib
import os
import sqlite3
from io import BytesIO

from chromadb.errors import ChromaError
from dotenv import load_dotenv
from fastapi import FastAPI, File, Form, HTTPException, UploadFile
from fastapi.middleware.cors import CORSMiddleware
from pypdf import PdfReader
from pypdf.errors import PdfReadError

from models.schemas import QuestionRequest, AnswerResponse
from services.chroma_service import document_hash_exists
from services.ingestion_service import ingest_document
from services.rag_service import ask_rag


load_dotenv()

frontend_url = os.getenv("FRONTEND_URL")


app = FastAPI(
    title="Enterprise AI Assistant API"
)


app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        frontend_url
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
def home():
    return {
        "message": "Enterprise AI Assistant API is running"
    }


@app.post("/api/ask", response_model=AnswerResponse)
def ask_question(data: QuestionRequest):

    result = ask_rag(data.question)

    return AnswerResponse(
        answer=result["answer"],
        sources=result["sources"]
    )


@app.post("/api/documents/upload")
async def upload_document(
    file: UploadFile = File(...),
    department: str = Form("General"),
):
    filename = file.filename or ""
    if not filename.lower().endswith(".pdf"):
        raise HTTPException(
            status_code=400,
            detail="Only PDF files can be uploaded.",
        )

    file_contents = await file.read()
    if not file_contents:
        raise HTTPException(
            status_code=400,
            detail="The uploaded PDF is empty.",
        )

    document_hash = hashlib.sha256(file_contents).hexdigest()
    try:
        if document_hash_exists(document_hash):
            return {
                "message": "Document already indexed",
                "filename": filename,
            }
    except (ChromaError, OSError, sqlite3.Error) as error:
        raise HTTPException(
            status_code=500,
            detail="Could not check whether the document was already indexed.",
        ) from error

    try:
        reader = PdfReader(BytesIO(file_contents))
        if reader.is_encrypted:
            raise HTTPException(
                status_code=400,
                detail="Encrypted PDFs are not supported.",
            )

        if not reader.pages:
            raise HTTPException(
                status_code=422,
                detail="The uploaded PDF contains no pages.",
            )

        pages = [
            (page_number, page.extract_text() or "")
            for page_number, page in enumerate(reader.pages, start=1)
        ]
    except PdfReadError as error:
        raise HTTPException(
            status_code=400,
            detail="Could not read the PDF. Please upload a valid, unencrypted PDF.",
        ) from error
    except (OSError, ValueError) as error:
        raise HTTPException(
            status_code=400,
            detail="Could not read the PDF. Please upload a valid, unencrypted PDF.",
        ) from error

    if not any(text.strip() for _, text in pages):
        raise HTTPException(
            status_code=422,
            detail="No extractable text was found in the PDF.",
        )

    try:
        result = ingest_document(
            pages=pages,
            filename=filename,
            document_hash=document_hash,
            department=department.strip() or "General",
        )
    except ValueError as error:
        raise HTTPException(status_code=422, detail=str(error)) from error
    except (ChromaError, OSError, sqlite3.Error) as error:
        raise HTTPException(
            status_code=500,
            detail="The PDF was read, but its document chunks could not be saved.",
        ) from error

    return {
        "message": "Document uploaded and indexed successfully.",
        **result,
    }