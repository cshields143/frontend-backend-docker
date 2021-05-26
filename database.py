from sqlalchemy import create_engine, Column, Integer
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
engine = create_engine("postgres://myuser:mypassword@backend/mydb")
Session = sessionmaker(autocommit=False, autoflush=False, bind=engine)
BaseModel = declarative_base()
class Thingy(BaseModel):
    __tablename__ = "thingies"
    id = Column(Integer, primary_key=True)
