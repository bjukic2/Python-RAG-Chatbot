from fastapi import APIRouter
from fastapi.responses import StreamingResponse
from pydantic import BaseModel
from app.rag.pipeline import RAGPipeline

router = APIRouter(tags=["chat"])
pipeline = RAGPipeline()

class ChatRequest(BaseModel):
    message: str


@router.post("/chat/stream")
async def chat_stream(request: ChatRequest):

    async def event_generator():
        async for token in pipeline.run_stream(request.message):
            # mora biti bytes, ne string
            yield token.encode("utf-8")

    return StreamingResponse(
        event_generator(),
        media_type="text/event-stream"
    )
