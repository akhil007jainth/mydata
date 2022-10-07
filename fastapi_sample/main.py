from fastapi import FastAPI, Depends, HTTPException, status, Security
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from sqlalchemy import false
from schemas import Todo, user, update_todo, delete_todo
from sqlalchemy.orm import Session
import models
from models import todotable, usertable
from sqldb import engine, get_db
from hash import Hash
from jose import jwt, JWTError
from typing import Optional
from datetime import datetime, timedelta
from hash import create_access_token, verify_token

app = FastAPI()
# this api for login


@app.post('/login')
async def login(request: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    check = db.query(usertable).filter(
        usertable.username == request.username).first()
    if not check:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail=f"Invalid Credentials"
        )
    a = Hash.verify(check.password, request.password)
    if not a:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail=f"Incorrect password"
        )
    try:
        token = create_access_token(data={"sub": check.username})
    except:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail=f"Incorrect password"
        )

    return {"access_token": token, "token_type": "bearer"}


# this api for register the new user
@app.post('/register')
async def register(user: user, db: Session = Depends(get_db)):
    hashed_password = Hash.bcrypt(user.password)

    userdata = usertable(username=user.username, password=hashed_password)
    db.add(userdata)
    db.commit()
    db.refresh(userdata)
    return {"user added"}

# this api for add todo

@app.post('/add_item')
async def add_todo(user: Todo, db: Session = Depends(get_db), token: str = Depends(verify_token)):
    todo_item = todotable(Name=user.Name, Todo_Title=user.Todo_Title,
                          Todo_Description=user.Todo_Description)
    db.add(todo_item)
    db.commit()
    db.refresh(todo_item)
    return {"todo added": user}

# for update todo

@app.put('/update_item')
async def update_todo(user: update_todo, db: Session = Depends(get_db), token: str = Depends(verify_token)):
    todo_item = db.query(todotable).filter(todotable.id == user.id).first()
    todo_item.Name = user.Name
    todo_item.Todo_Title = user.Todo_Title
    todo_item.Todo_Description = user.Todo_Description
    db.commit()
    db.refresh(todo_item)
    return {"updated todo": todo_item}

#  for delete todo

@app.delete('/delete_item')
async def delete_item(user: delete_todo, db: Session = Depends(get_db), token: str = Depends(verify_token)):
    todo_item = db.query(todotable).filter(
        todotable.id == user.id).delete(synchronize_session=False)

    db.commit()

    return {"deleted todo"}

# this api for show all todos list


@app.get('/show_all_item')
async def show_all_todo(db: Session = Depends(get_db), token: str = Depends(verify_token)):
    id = db.query(todotable).all()
    return {"data": id}

# this api for show one todo by id


@app.get('/show_one_todo')
async def show_one_todo(todo_id: int, db: Session = Depends(get_db), token: str = Depends(verify_token)):
    id1 = db.query(todotable).filter(todotable.id == todo_id).first()
    return {"data": id1}

models.Base.metadata.create_all(bind=engine)
