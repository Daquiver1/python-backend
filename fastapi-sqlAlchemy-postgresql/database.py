from dotenv import load_dotenv
import os
from sqlalchemy.orm import declarative_base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

load_dotenv()
SQL_USERNAME = os.getenv("SQL_USERNAME")
SQL_PASSWORD = os.getenv("SQL_PASSWORD")

engine = create_engine(F"postgresql://{SQL_USERNAME}:{SQL_PASSWORD}@localhost/item_db", echo=True)

Base = declarative_base()

SessionLocal = sessionmaker(bind=engine)

