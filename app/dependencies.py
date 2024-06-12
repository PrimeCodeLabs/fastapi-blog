from app.db import SessionLocal
from fastapi import Request, HTTPException

async def validate_payload_size(request: Request):
    content_length = request.headers.get('content-length')
    if content_length and int(content_length) > 1024 * 1024:
        raise HTTPException(status_code=413, detail="Payload too large")

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
