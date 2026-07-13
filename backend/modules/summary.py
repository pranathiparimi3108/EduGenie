from ai.gemini_model import GeminiModel


def summarize_content(content: str) -> str:
    model = GeminiModel()
    prompt = (
        "Summarize the following study content into concise bullet points "
        "with key terms and revision tips:\n\n"
        f"{content}"
    )
    return model.generate(prompt)
