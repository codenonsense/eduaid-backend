from fastapi import APIRouter, HTTPException

from utils.prompt_utils import qna_prompt
from services.qna_service import answer_qna

qna_router = APIRouter()

@qna_router.get('/qna')
async def get_qna(name, summary, question):
    prompt = qna_prompt(name=name, question=question, summary=summary)
    response = answer_qna(prompt)
    raise HTTPException(status_code=200, detail=f"{response}")
