import logging

from sqlalchemy import select
from sqlalchemy.orm import Session

from app.models.meeting import Meeting

logger = logging.getLogger(__name__)


class MeetingRepository:
    def __init__(self, session: Session):
        self.session = session
        logger.debug("MeetingRepository initialized")

    def create(self, meeting: Meeting) -> Meeting:
        """Save a meeting to the database."""
        logger.info("Persisting meeting: %s", meeting.title)
        self.session.add(meeting)
        self.session.commit()
        self.session.refresh(meeting)
        logger.info("Persisted meeting id=%s", meeting.id)
        return meeting

    def get_all(self) -> list[Meeting]:
        """Return all meetings, ordered by creation time."""
        logger.info("Querying all meetings")
        statement = select(Meeting).order_by(Meeting.created_at.desc())
        meetings = self.session.scalars(statement).all()
        logger.info("Retrieved %s meetings", len(meetings))
        return meetings

    def get_by_id(self, meeting_id: int) -> Meeting | None:
        """Return a meeting by its numeric ID."""
        logger.info("Querying meeting by id=%s", meeting_id)
        return self.session.get(Meeting, meeting_id)
