from datetime import datetime
from typing import Optional

from pydantic import BaseModel, Field


class MeetingCreate(BaseModel):
    """Input data when a meeting is created."""
    title: str = Field(..., min_length=1)
    notes: str = Field(..., min_length=1)
    source: Optional[str] = "manual"


class MeetingRead(BaseModel):
    """Response model for meeting details."""
    id: int
    title: str
    notes: str
    summary: Optional[str]
    source: str
    created_at: datetime

    class Config:
        orm_mode = True


class AskRequest(BaseModel):
    """Input data for asking a question."""
    question: str = Field(..., min_length=1)


class AskResponse(BaseModel):
    """Response format for question answers."""
    question: str
    answer: str
    context: Optional[str]
