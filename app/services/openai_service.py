import logging

from app.core.config import settings

logger = logging.getLogger(__name__)


class OpenAIService:
    def __init__(self):
        self.api_key = settings.openai_api_key

    def summarize(self, title: str, notes: str) -> str:
        logger.info("OpenAI summarize called")
        if not self.api_key:
            logger.warning("No OpenAI API key configured; using fallback summary")
            return f"Summary for meeting '{title}' with {len(notes.split())} words."

        try:
            import openai

            openai.api_key = self.api_key
            prompt = (
                f"Summarize the following meeting notes into a short paragraph.\nTitle: {title}\nNotes:\n{notes}\n"
            )
            response = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",
                messages=[{"role": "user", "content": prompt}],
                max_tokens=150,
                temperature=0.3,
            )
            return response.choices[0].message.content.strip()
        except Exception as exc:
            logger.exception("OpenAI API failed")
            return f"Unable to generate summary: {exc}"
