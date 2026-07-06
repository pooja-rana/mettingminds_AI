# MeetingMind AI

An AI-powered Meeting Memory Assistant that stores meeting notes, generates summaries, and answers questions over meeting content.

## Problem Statement

Meetings often produce a lot of useful information, but it is difficult to find later. Team members lose time searching notes for decisions, action items, or follow-up details.

Why this is frustrating:

- meeting notes are hard to search and revisit
- summaries are inconsistent or missing
- follow-up decisions are buried in text

Who experiences this problem:

- product managers
- engineering teams
- project leads
- remote and distributed teams

## Thought Process

I designed MeetingMind AI as a backend-first application to maximize delivery in a short timeframe. The goal was to show a working API with structured storage, AI-powered summarization, and question answering.

Alternative ideas considered:

- adding a full frontend dashboard
- supporting audio transcription
- building a multi-user authentication system

Trade-offs:

- chose SQLite for ease of setup
- used a mock semantic search layer for rapid delivery
- kept the API simple and extensible

## Solution Overview

MeetingMind AI includes:

- `POST /meetings/` to save meeting notes and generate a summary
- `GET /meetings/` to list stored meetings
- `GET /meetings/{meeting_id}` to retrieve meeting details
- `POST /ask/` to ask a question over meeting context

The backend uses:

- FastAPI for HTTP routing
- SQLAlchemy ORM with SQLite for persistence
- OpenAI for summary generation
- a mocked semantic search component for question context

## Technology Choices

- Python 3.14: modern syntax and runtime support
- FastAPI: fast developer experience with automatic docs
- SQLAlchemy: reliable ORM for persistence
- SQLite: lightweight, zero-configuration database
- OpenAI: AI-generated meeting summaries
- Docker / docker-compose: container support for deployment
- pytest: automated testing

## Architecture

See `ARCHITECTURE.md` for the component diagram.

## Installation

1. Create a virtual environment:
   ```bash
   python3 -m venv .venv
   source .venv/bin/activate
   ```
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Set environment variables in `.env` if using OpenAI:
   ```bash
   OPENAI_API_KEY=your_api_key
   ```

## Run

```bash
cd meetingmind-ai
uvicorn app.main:app --reload
```

Open `http://127.0.0.1:8000/docs` for API documentation.
## Docker

From the `meetingmind-ai` directory:

```bash
docker compose up --build
```

The app will be available at `http://127.0.0.1:8000`.
## Testing

Run the test suite:

```bash
cd meetingmind-ai
source .venv/bin/activate
pytest -q
```

## Demo Script

See `DEMO.md` for a short walkthrough of the project.

## Future Improvements

- add user authentication and profiles
- integrate a real vector database like Chroma
- support meeting transcript ingestion
- build a frontend dashboard
- add tagging, pagination, and meeting search
