from database import Base
from sqlalchemy import Boolean, Column, Integer, String

class Todo(Base):
    __tablename__ = "todos"
 
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String)
    complete = Column(Boolean, default=False)