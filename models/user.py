from pydantic import BaseModel
from typing import List, Dict, Optional
from bson import ObjectId

class SignupModel(BaseModel):
    username:str 
    email:str 
    password:str 

class LoginModel(BaseModel):
    email:str 
    password:str

class Progress(BaseModel):
    completed_videos: List[str] = [] 
    current_learning_path: str = None 
    quiz_scores: Dict[str, int] = {}


class UserModel(BaseModel):
    id: Optional[str] = ObjectId
    username:str 
    email:str
    password:str
    progress: Progress
