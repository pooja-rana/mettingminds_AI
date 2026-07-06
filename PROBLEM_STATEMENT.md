# MeetingMind AI - Problem Statement

## Problem

Meetings often produce valuable information, but that information is difficult to revisit. Notes are typically stored as plain text, and tracking decisions, action items, and follow-ups becomes time-consuming.

## Why it is frustrating

- Meeting notes become hard to search long after the meeting.
- Key decisions and action items are buried in unstructured text.
- Teams waste time re-reading notes instead of moving forward.

## Who experiences this problem

- product managers
- engineering teams
- project leads
- remote and distributed teams

## Proposed solution

MeetingMind AI stores meeting notes and generates a short summary for each meeting. It also supports asking questions over saved meeting context, helping users quickly recall decisions and action items.

## Technical approach

- Backend API using FastAPI
- SQLite persistence using SQLAlchemy
- Meeting summary generation using OpenAI
- Question answering support with a mock semantic search service
- Containerization via Docker and Docker Compose

## Future improvements

- add real vector database support for semantic search
- support meeting transcription ingestion
- add authentication and multi-user support
- build a user-facing frontend dashboard
- enhance note search and tagging
