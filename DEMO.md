# Demo Walkthrough

This demo script helps you show the project quickly during the interview.

1. Start the application:
   ```bash
   cd meetingmind-ai
   source .venv/bin/activate
   uvicorn app.main:app --reload
   ```

2. Open the API docs:
   - `http://127.0.0.1:8000/docs`

3. Create a meeting:
   - `POST /meetings/`
   - Example payload:
     ```json
     {
       "title": "Sprint planning",
       "notes": "Discuss quarterly objectives and assign action items."
     }
     ```

4. Show the generated summary in the response.

5. List meetings:
   - `GET /meetings/`

6. Ask a question:
   - `POST /ask/`
   - Example payload:
     ```json
     {"question": "What did we decide about action items?"}
     ```

7. Explain the architecture:
   - FastAPI handles HTTP requests
   - SQLAlchemy stores meetings in SQLite
   - OpenAI generates meeting summaries
   - The question endpoint returns context and an answer

8. Mention future improvements:
   - real embedding store
   - audio transcription input
   - frontend UI
   - authentication / user management
