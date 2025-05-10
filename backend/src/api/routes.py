from fastapi import APIRouter

from src.schemas.request_models import QueryRequest
from src.services.live_text_client import get_text_response_live

router = APIRouter()


@router.get("/")
async def root():
    return {"message": "FastAPI is working!"}


@router.post("/text-query-live")
async def handle_text_query_live(request: QueryRequest):
    response = await get_text_response_live(request.prompt)
    return {"user_id": request.user_id, "prompt": request.prompt, "response": response}
