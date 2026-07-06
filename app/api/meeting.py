import logging

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.dependencies import get_meeting_repository
from app.schemas.meeting import MeetingCreate, MeetingRead
from app.repositories.meeting_repository import MeetingRepository
from app.services.meeting_service import MeetingService

logger = logging.getLogger(__name__)
router = APIRouter(prefix="/meetings", tags=["meetings"])


@router.post("/", response_model=MeetingRead)
def create_meeting(meeting_create: MeetingCreate, repository: MeetingRepository = Depends(get_meeting_repository)):
    logger.info("Received request to create meeting: %s", meeting_create.title)
    meeting_service = MeetingService(repository)
    meeting = meeting_service.create_meeting(meeting_create)
    logger.info("Meeting created with id=%s", meeting.id)
    return meeting


@router.get("/", response_model=list[MeetingRead])
def list_meetings(repository: MeetingRepository = Depends(get_meeting_repository)):
    logger.info("Received request to list meetings")
    meeting_service = MeetingService(repository)
    meetings = meeting_service.list_meetings()
    logger.info("Returning %s meetings", len(meetings))
    return meetings


@router.get("/{meeting_id}", response_model=MeetingRead)
def get_meeting(meeting_id: int, repository: MeetingRepository = Depends(get_meeting_repository)):
    logger.info("Received request to get meeting id=%s", meeting_id)
    meeting = repository.get_by_id(meeting_id)
    if not meeting:
        logger.warning("Meeting not found: id=%s", meeting_id)
        raise HTTPException(status_code=404, detail="Meeting not found")
    return meeting
