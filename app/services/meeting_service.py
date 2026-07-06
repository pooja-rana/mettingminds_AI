import logging

from app.models.meeting import Meeting
from app.repositories.meeting_repository import MeetingRepository
from app.schemas.meeting import MeetingCreate
from app.services.openai_service import OpenAIService
from app.services.chroma_service import ChromaService

logger = logging.getLogger(__name__)


class MeetingService:
    def __init__(self, repository: MeetingRepository):
        self.repository = repository
        self.openai_service = OpenAIService()
        self.chroma_service = ChromaService()

    def create_meeting(self, meeting_create: MeetingCreate):
        """Create a meeting record with an AI-generated summary."""
        summary = self.openai_service.summarize(meeting_create.title, meeting_create.notes)
        meeting = Meeting(
            title=meeting_create.title,
            notes=meeting_create.notes,
            source=meeting_create.source,
            summary=summary,
        )
        meeting = self.repository.create(meeting)
        logger.info("Meeting created with summary")
        return meeting

    def list_meetings(self):
        """Return all meetings from storage."""
        return self.repository.get_all()

    def ask_question(self, question: str):
        """Use the semantic search layer to answer a question."""
        context = self.chroma_service.search(question)
        answer = f"Answer for: {question}. Context: {'; '.join(context)}"
        return question, answer, "; ".join(context)
