from ai.gemini_model import GeminiModel


def explain_topic(topic: str, level: str = "beginner") -> str:
    model = GeminiModel()
    prompt = (
        f"Explain the topic '{topic}' for a {level} learner. "
        "Use simple language, short sections, and one real-world example."
    )
    return model.generate(prompt)
