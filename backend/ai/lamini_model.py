"""Optional local/fallback model hook for future offline inference."""

from ai.gemini_model import GeminiModel


class LaminiModel:
    """Currently delegates to Gemini. Replace with a local model when available."""

    def __init__(self):
        self._model = GeminiModel()

    def generate(self, prompt: str) -> str:
        return self._model.generate(prompt)
