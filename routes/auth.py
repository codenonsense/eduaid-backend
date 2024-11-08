from fastapi import APIRouter, Depends, HTTPException

from db import mongo_connect
from models.user import SignupModel, LoginModel
from utils.auth_utils import check_password, hash_password, generate_token

auth_router = APIRouter()

@auth_router.post('/signup')
async def signup(user:SignupModel, db = Depends(mongo_connect)):

    hashed_password = hash_password(user.password)
    user_payload = {
        "username": user.username,
        "email": user.email,
        "password": hashed_password,
        "progress": { "completed_videos": [], "current_learning_path": None, "quiz_scores": [] }
    }
    try:
        db['users'].insert_one(user_payload)
        raise HTTPException(status_code=200, detail="Account Creation Successful")
    except:
        raise HTTPException(status_code=500, detail="Internal Server Error")
    
@auth_router.post('/login')
async def login(user:LoginModel, db = Depends(mongo_connect)):
    user_exists = db['users'].find({"email": user.email})
    if user_exists:
        user_dict = db['users'].find({"email":user.email})
        for data in user_dict:
            hashed_password = data["password"]
            print(hashed_password)
            check_password(password=user.password, hashed_password=hashed_password)
            token = generate_token()
            raise HTTPException(status_code=200, detail=f"{token}")