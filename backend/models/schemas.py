from pydantic import BaseModel


class QuestionRequest(BaseModel):
    question: str


class Source(BaseModel):
    title: str
    page: int
    department: str


class AnswerResponse(BaseModel):
    answer: str
    sources: list[Source]