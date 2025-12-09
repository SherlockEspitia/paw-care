from datetime import datetime, timedelta
from jose import JWTError, jwt
from passlib.context import CryptContext
from fastapi.security import OAuth2PasswordBearer
from app.utils.settings import Settings

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

def verify_password(plain, hashed): 
    return pwd_context.verify(plain, hashed)

def get_password_hash(password): 
    return pwd_context.hash(password)

def create_access_token(data: dict, expires_delta: timedelta = None):
    to_encode = data.copy()
    if expires_delta: 
        to_encode.update({"exp": datetime.now(datetime.timezone.utc) + expires_delta})
    
    return jwt.encode(to_encode, Settings.secret_key, algorithm=Settings.algorithm)

