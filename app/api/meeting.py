from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.dependencies import get_meeting_repository
from app.schemas.meeting import MeetingCreate, MeetingRead
from app.repositories.meeting_repository import MeetingRepository
from app.services.meeting_service import MeetingService

router = APIRouter(prefix="/meetings", tags=["meetings"])


@router.post("/", response_model=MeetingRead)
def create_meeting(meeting_create: MeetingCreate, repository: MeetingRepository = Depends(get_meeting_repository)):
    meeting_service = MeetingService(repository)
    return meeting_service.create_meeting(meeting_create)


@router.get("/", response_model=list[MeetingRead])
def list_meetings(repository: MeetingRepository = Depends(get_meeting_repository)):
    meeting_service = MeetingService(repository)
    return meeting_service.list_meetings()


@router.get("/{meeting_id}", response_model=MeetingRead)
def get_meeting(meeting_id: int, repository: MeetingRepository = Depends(get_meeting_repository)):
    meeting = repository.get_by_id(meeting_id)
    if not meeting:
        raise HTTPException(status_code=404, detail="Meeting not found")
    return meeting
