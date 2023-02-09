from app.database import SessionLocal

#FastAPI Dependencies: https://fastapi.tiangolo.com/tutorial/dependencies

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close