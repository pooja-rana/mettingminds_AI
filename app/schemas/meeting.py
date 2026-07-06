from datetime import datetime
from typing import Optional

from pydantic import BaseModel, Field


class MeetingCreate(BaseModel):
    title: str = Field(..., min_length=1)
    notes: str = Field(..., min_length=1)
    source: Optional[str] = "manual"


class MeetingRead(BaseModel):
    id: int
    title: str
    notes: str
    summary: Optional[str]
    source: str
    created_at: datetime

    class Config:
        orm_mode = True


class AskRequest(BaseModel):
    question: str = Field(..., min_length=1)


class AskResponse(BaseModel):
    question: str
    answer: str
    context: Optional[str]
