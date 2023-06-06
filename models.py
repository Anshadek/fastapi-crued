from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship
from database import Base

# Define To Do class inheriting from Base
class ToDo(Base):
    __tablename__ = 'todos'
    id = Column(Integer, primary_key=True)
    task = Column(String(256))

class Language(Base):
    __tablename__ = 'language'
    id = Column(Integer, primary_key=True)
    name = Column(String(256))

class Project(Base):
    __tablename__ = 'project'
    id = Column(Integer, primary_key=True)
    name = Column(String(256))

class EmpUser(Base):
    __tablename__ = 'emp_user'
    id = Column(Integer, primary_key=True)
    user_name = Column(String(256))
    email = Column(String(250), unique=True, index=True)
    hashed_password = Column(String(250))
    lang_id = Column(Integer, ForeignKey("language.id"))


class UserProject(Base):
    __tablename__ = 'user_projects'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey("emp_user.id"))
    project_id = Column(Integer, ForeignKey("project.id"))

