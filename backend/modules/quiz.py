"""
Quiz Module for EduGenie

This module generates AI-powered multiple-choice quizzes
using Google Gemini AI.
"""

from ai.gemini_model import GeminiModel


def generate_quiz(topic: str, num_questions: int = 5) -> str:
    """
    Generate a multiple-choice quiz for the given topic.

    Args:
        topic (str): Topic for quiz generation.
        num_questions (int): Number of questions to generate.

    Returns:
        str: AI-generated quiz with answers and explanations.
    """

    if not topic.strip():
        return "Error: Please enter a valid topic."

    model = GeminiModel()

    prompt = f"""
You are an expert educator.

Generate {num_questions} high-quality multiple-choice questions on the topic "{topic}".

Instructions:
1. Questions should progress from easy to difficult.
2. Each question must have exactly four options:
   A)
   B)
   C)
   D)
3. Clearly indicate the correct answer.
4. Provide a one-line explanation for the correct answer.
5. Avoid duplicate questions.
6. Use simple and student-friendly language.
7. Format the output neatly.

Example Format:

Question 1:
What is ...?

A)
B)
C)
D)

Correct Answer: B

Explanation:
...

Repeat this format for all questions.
"""

    try:
        return model.generate(prompt)

    except Exception as e:
        return f"Quiz generation failed: {str(e)}"
