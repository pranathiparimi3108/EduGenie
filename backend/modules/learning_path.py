from ai.gemini_model import GeminiModel


def generate_learning_path(topic: str, duration_days: int = 7) -> str:
    model = GeminiModel()
    prompt = (
        f"Create a {duration_days}-day personalized learning path for '{topic}'. "
        "Return numbered daily goals, resources to study, and a short practice task for each day."
    )
    return model.generate(prompt)
