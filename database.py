from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


DATABASE_URL = "mysql+mysqlconnector://root@localhost:3306/todo"
engine = create_engine(DATABASE_URL)

# Create a DeclarativeMeta instance
Base = declarative_base()


# Create SessionLocal class from sessionmaker factory
SessionLocal = sessionmaker(bind=engine, expire_on_commit=False)