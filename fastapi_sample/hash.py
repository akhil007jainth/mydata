from passlib.context import CryptContext
from jose import jwt, JWTError
from typing import Optional
from datetime import datetime, timedelta
from sqldb import get_db
from sqlalchemy.orm import Session
from fastapi import Depends,HTTPException,status
from models import usertable
from fastapi.security import OAuth2PasswordBearer,OAuth2PasswordRequestForm

pwd_ctx = CryptContext(schemes=["bcrypt"], deprecated="auto")

t=OAuth2PasswordBearer(tokenUrl='/login')

class Hash:
    def bcrypt(password: str):
        return pwd_ctx.hash(password)

    def verify(hashed_password, plain_password):
        return pwd_ctx.verify(plain_password, hashed_password)
def create_access_token(data: dict, expires_delta: Optional[timedelta] = None):
            to_encode = data.copy()
    
            encoded_jwt = jwt.encode(to_encode, key="", algorithm="HS256")
            return encoded_jwt
def verify_token(token: str = Depends(t), db: Session = Depends(get_db)):

    try:
        payload = jwt.decode(token, key="", algorithms="HS256")

        username: str = payload.get("sub")
    except JWTError:
         raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail=f"Incorrect Token"
        )
    

    user = db.query(usertable).filter(usertable.username == username).first()

    if user.username!=username:
         raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail=f"invalid user"
        )

    return {"success"}