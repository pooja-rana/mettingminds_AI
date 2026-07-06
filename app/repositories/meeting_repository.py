from sqlalchemy import select
from sqlalchemy.orm import Session

from app.models.meeting import Meeting


class MeetingRepository:
    def __init__(self, session: Session):
        self.session = session

    def create(self, meeting: Meeting) -> Meeting:
        self.session.add(meeting)
        self.session.commit()
        self.session.refresh(meeting)
        return meeting

    def get_all(self) -> list[Meeting]:
        statement = select(Meeting).order_by(Meeting.created_at.desc())
        return self.session.scalars(statement).all()

    def get_by_id(self, meeting_id: int) -> Meeting | None:
        return self.session.get(Meeting, meeting_id)
