from fastapi import APIRouter
from pydantic import BaseModel
from app.rag.pipeline import RAGPipeline

router = APIRouter(tags=["chat"])
pipeline = RAGPipeline()

class ChatRequest(BaseModel):
    message: str

class ChatResponse(BaseModel):
    answer: str

@router.post("/chat", response_model=ChatResponse)
async def chat(request: ChatRequest):
    answer = pipeline.run(request.message)
    return ChatResponse(answer=answer)