import logging

from fastapi import APIRouter, Depends

from app.dependencies import get_meeting_repository
from app.schemas.meeting import AskRequest
from app.repositories.meeting_repository import MeetingRepository
from app.services.meeting_service import MeetingService

logger = logging.getLogger(__name__)
router = APIRouter(prefix="/ask", tags=["ask"])


@router.post("/", response_model=dict)
def ask_question(request: AskRequest, repository: MeetingRepository = Depends(get_meeting_repository)):
    """Answer a question using the stored meeting context."""
    logger.info("Received ask request: %s", request.question)
    meeting_service = MeetingService(repository)
    question, answer, context = meeting_service.ask_question(request.question)
    logger.info("Returning answer for question")
    return {"question": question, "answer": answer, "context": context}
