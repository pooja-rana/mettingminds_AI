# MeetingMind AI

A docker-ready AI meeting memory assistant backend.

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

## Run Locally

```bash
cd meetingmind-ai
uvicorn app.main:app --reload
```

Open `http://127.0.0.1:8000/docs` for API docs.

## Run with Docker

```bash
docker compose up --build
```

Open `http://127.0.0.1:8000`.

## Testing

```bash
cd meetingmind-ai
source .venv/bin/activate
pytest -q
```

## Documentation

- `ARCHITECTURE.md` - architecture overview
- `DEMO.md` - demo walkthrough script
- `PROBLEM_STATEMENT.md` - project problem statement and solution description
