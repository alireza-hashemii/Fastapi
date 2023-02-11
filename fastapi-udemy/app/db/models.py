from sqlalchemy.schema import ForeignKey
from .database import Base
from sqlalchemy import Column, Integer, String , Boolean
from sqlalchemy.orm.relationships import RelationshipProperty


class DbUser(Base):
  __tablename__ = 'users'
  id = Column(Integer, primary_key=True, index=True)
  username = Column(String)
  email = Column(String)
  password = Column(String)
  items = RelationshipProperty("ArticleTable",back_populates='user')
  
class ArticleTable(Base):
  __tablename__ = 'articles'
  id =  Column(Integer, primary_key=True, index=True)
  title = Column(String)
  content = Column(String)
  published = Column(Boolean)
  user_id = Column(String,ForeignKey("users.id"))
  user = RelationshipProperty("DbUser",back_populates='items')
  

    
  