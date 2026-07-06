import logging

from fastapi import Depends

from app.core.database import SessionLocal
from app.repositories.meeting_repository import MeetingRepository

logger = logging.getLogger(__name__)


def get_db():
    logger.debug("Opening new database session")
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
        logger.debug("Database session closed")


def get_meeting_repository(db=Depends(get_db)):
    return MeetingRepository(db)
