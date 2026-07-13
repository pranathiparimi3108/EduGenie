from ai.gemini_model import GeminiModel


def generate_quiz(topic: str, num_questions: int = 5) -> str:
    model = GeminiModel()
    prompt = (
        f"Create {num_questions} multiple-choice questions on '{topic}'. "
        "For each question provide: question, 4 options (A-D), correct answer, and a one-line explanation."
    )
    return model.generate(prompt)
