from fastapi import APIRouter, Depends

from app.dependencies import get_meeting_repository
from app.schemas.meeting import AskRequest
from app.repositories.meeting_repository import MeetingRepository
from app.services.meeting_service import MeetingService

router = APIRouter(prefix="/ask", tags=["ask"])


@router.post("/", response_model=dict)
def ask_question(request: AskRequest, repository: MeetingRepository = Depends(get_meeting_repository)):
    meeting_service = MeetingService(repository)
    question, answer, context = meeting_service.ask_question(request.question)
    return {"question": question, "answer": answer, "context": context}
