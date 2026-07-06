import logging

from app.core.config import settings

logger = logging.getLogger(__name__)


class ChromaService:
    def __init__(self):
        self.collection_name = settings.chroma_collection

    def embed(self, text: str) -> list[float]:
        logger.info("Generating embedding for text")
        try:
            import numpy as np

            vector = np.random.normal(size=384).tolist()
            return vector
        except ImportError:
            logger.warning("Numpy not installed; returning empty embedding")
            return []

    def search(self, query: str, top_k: int = 3) -> list[str]:
        logger.info("Running approximate semantic search")
        return [f"Mocked related note for query: {query}"]
