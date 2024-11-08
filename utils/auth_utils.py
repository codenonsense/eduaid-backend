
from passlib.context import CryptContext
import jwt


pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
def hash_password(password):
    return pwd_context.hash(password)

def check_password(hashed_password, password):
    return pwd_context.verify(password, hashed_password)

def generate_token(payload):
    secret_key = "eduaidiseduaid"
    token = jwt.encode(payload, secret_key, "HS256")
    return token
