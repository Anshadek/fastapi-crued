from pydantic import BaseModel

# Create ToDo Schema (Pydantic Model)
class ToDoCreate(BaseModel):
    task: str

# Complete ToDo Schema (Pydantic Model)
class ToDo(BaseModel):
    id: int
    task: str

    class Config:
        orm_mode = True


class LanguageCreate(BaseModel):
     name: str

     
class Language(BaseModel):
    id: int
    name: str

    class Config:
        orm_mode = True

class Project(BaseModel):
    id: int
    name: str

    class Config:
        orm_mode = True


class EmpUser(BaseModel):
    id: int
    user_name:str
    email: str
    hashed_password:str
    lang_id:int
    task: str

    class Config:
        orm_mode = True


class UserProject(BaseModel):
    id: int
    user_id : int
    project_id : int
    name: str

    class Config:
        orm_mode = True

    