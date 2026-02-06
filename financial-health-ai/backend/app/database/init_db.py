from app.database.database import engine
from app.models.financial_model import Financial
from app.models.user_model import User
from app.database.database import Base

print("Creating tables...")

Base.metadata.create_all(bind=engine)

print("Tables created successfully!")
