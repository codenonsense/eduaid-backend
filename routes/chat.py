from fastapi import APIRouter, HTTPException

from utils.prompt_utils import qna_prompt
from services.chat_service import get_chat_text

chat_router = APIRouter()

@chat_router.get('/chat')
async def get_qna(convtext):
    prompt = convtext
    response = get_chat_text(prompt)
    raise HTTPException(status_code=200, detail=f"{response}")
