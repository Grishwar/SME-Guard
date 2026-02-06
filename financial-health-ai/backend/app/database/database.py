from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
import os
from dotenv import load_dotenv

load_dotenv()

DATABASE_URL = os.getenv("DATABASE_URL")

# ✅ Prevents DB connection crashes
engine = create_engine(
    DATABASE_URL,
    pool_pre_ping=True   # VERY IMPORTANT
)

SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine
)

Base = declarative_base()


# ✅ Clean DB session (no memory leaks)
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
