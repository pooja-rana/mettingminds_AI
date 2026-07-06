import logging

from fastapi import FastAPI
from app.core.logging import configure_logging
from app.core.database import engine
from app.models.meeting import Base
from app.api.meeting import router as meeting_router
from app.api.ask import router as ask_router
from app.core.config import settings

configure_logging()
logger = logging.getLogger(__name__)
Base.metadata.create_all(bind=engine)

app = FastAPI(title=settings.app_name)
app.include_router(meeting_router)
app.include_router(ask_router)

logger.info("Starting MeetingMind AI application")

@app.get("/", tags=["root"])
def root():
    logger.info("Root endpoint accessed")
    return {"message": "Welcome to MeetingMind AI"}
