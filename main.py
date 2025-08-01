
from sqlalchemy import create_engine # type: ignore
from sqlalchemy.orm import sessionmaker, declarative_base # type: ignore

db = create_engine('sqlite:///meubanco.db')
Session = sessionmaker(bind=db)
session = Session()



Base = declarative_base()
Base.metadata.create_all(bind=db)