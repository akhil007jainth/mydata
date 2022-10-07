from pydantic import BaseModel
from typing import Optional

class user(BaseModel):
    username:str
    password:str
class Todo(BaseModel):
    Name:str
    Todo_Title:str
    Todo_Description:str
class update_todo(BaseModel):
    id:int
    Name:str
    Todo_Title:str
    Todo_Description:str
class delete_todo(BaseModel):
    id:int

