# Architecture

MeetingMind AI is a backend-focused project with a clean separation between API, services, repositories, and core configuration.

```
Client --> FastAPI app
            |
            +--> API routes (/meetings, /ask)
            |
            +--> MeetingService
                  |
                  +--> MeetingRepository --> SQLite
                  |
                  +--> OpenAIService --> OpenAI summary API
                  |
                  +--> ChromaService (mocked semantic search)
```

Components:

- `app/main.py`: app startup and router registration
- `app/api/`: REST endpoint handlers
- `app/services/`: business logic and AI service integration
- `app/repositories/`: database persistence
- `app/core/`: config, logging, database setup
- `app/schemas/`: request and response validation
