"""
Summary Module for EduGenie

Generates concise study notes using Google Gemini AI.
"""

from ai.gemini_model import GeminiModel


def summarize_content(content: str) -> str:
    """
    Generate a concise summary of the provided study content.

    Args:
        content (str): Text or study material to summarize.

    Returns:
        str: AI-generated summary with key points and revision tips.
    """

    if not content.strip():
        return "Error: Please provide valid study content."

    model = GeminiModel()

    prompt = f"""
You are an expert educational assistant.

Summarize the following study content in a clear and organized manner.

Instructions:
1. Begin with a short overview (2–3 sentences).
2. Present the important concepts as bullet points.
3. Highlight important keywords.
4. Include formulas or definitions if applicable.
5. Provide 3–5 quick revision tips.
6. Keep the summary concise, easy to understand, and exam-oriented.
7. Use simple language suitable for students.

Study Content:

{content}
"""

    try:
        return model.generate(prompt)

    except Exception as e:
        return f"Summary generation failed: {str(e)}"
