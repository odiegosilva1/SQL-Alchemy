
from sqlalchemy import create_engine, Column, String, Integer, Boolean, ForeignKey # type: ignore
from sqlalchemy.orm import sessionmaker, declarative_base # type: ignore

db = create_engine('sqlite:///meubanco.db')
Session = sessionmaker(bind=db)
session = Session()


Base = declarative_base


#add tables users
class Users(Base):
  id = Column("id", Integer)
  name = Column("name", String)
  email = Column("email", String)
  password = Column("password", String)
  active = Column("active", Boolean)

# add tables products
class Products(Base):
  id = Column("id", Integer)

Base = declarative_base()
Base.metadata.create_all(bind=db)