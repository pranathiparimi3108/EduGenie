from ai.gemini_model import GeminiModel


def answer_question(question: str, context: str = "") -> str:
    model = GeminiModel()
    prompt = (
        "You are EduGenie, a helpful study assistant. "
        f"Context: {context or 'General academics'}\n"
        f"Student question: {question}\n"
        "Give a clear, accurate, student-friendly answer."
    )
    return model.generate(prompt)
