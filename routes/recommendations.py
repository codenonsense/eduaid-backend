from fastapi import APIRouter, HTTPException

from db import mongo_connect
from utils.prompt_utils import recommendation_prompt


from database.data import Data

recommendation_router = APIRouter()

@recommendation_router.get('/recommend')
async def recommend(sub):
    print(sub)
    data = Data 
    matching_subject = [subject for subject in data if subject["subject"] == sub]
    if matching_subject == []:
        raise HTTPException(status_code=200, detail="No Videos Found")
    raise HTTPException(status_code=200, detail=f"{matching_subject}")
    

