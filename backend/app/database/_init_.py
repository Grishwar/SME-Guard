from app.database.database import engine
from app.models import financial_model, user_model

print("Creating tables...")

financial_model.Base.metadata.create_all(bind=engine)

print("Done.")
