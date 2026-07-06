from fastapi import Depends

from app.core.database import SessionLocal
from app.repositories.meeting_repository import MeetingRepository


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


def get_meeting_repository(db=Depends(get_db)):
    return MeetingRepository(db)
