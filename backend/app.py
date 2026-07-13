import os
import sys

from flask import Flask, jsonify, request, send_from_directory

sys.path.insert(0, os.path.dirname(__file__))

from config import Config
from modules.explanation import explain_topic
from modules.learning_path import generate_learning_path
from modules.quiz import generate_quiz
from modules.qna import answer_question
from modules.summary import summarize_content

app = Flask(__name__, static_folder="static", static_url_path="")
app.config.from_object(Config)


@app.route("/")
def index():
    return send_from_directory(app.static_folder, "index.html")


@app.route("/api/health", methods=["GET"])
def health():
    return jsonify({"status": "ok", "app": "EduGenie"})


@app.route("/api/explain", methods=["POST"])
def explain():
    data = request.get_json(silent=True) or {}
    topic = (data.get("topic") or "").strip()
    level = (data.get("level") or "beginner").strip()
    if not topic:
        return jsonify({"error": "Topic is required."}), 400
    try:
        result = explain_topic(topic, level)
        return jsonify({"topic": topic, "result": result})
    except Exception as exc:
        return jsonify({"error": str(exc)}), 500


@app.route("/api/learning-path", methods=["POST"])
def learning_path():
    data = request.get_json(silent=True) or {}
    topic = (data.get("topic") or "").strip()
    duration_days = int(data.get("duration_days") or 7)
    if not topic:
        return jsonify({"error": "Topic is required."}), 400
    try:
        result = generate_learning_path(topic, duration_days)
        return jsonify({"topic": topic, "result": result})
    except Exception as exc:
        return jsonify({"error": str(exc)}), 500


@app.route("/api/quiz", methods=["POST"])
def quiz():
    data = request.get_json(silent=True) or {}
    topic = (data.get("topic") or "").strip()
    num_questions = int(data.get("num_questions") or 5)
    if not topic:
        return jsonify({"error": "Topic is required."}), 400
    try:
        result = generate_quiz(topic, num_questions)
        return jsonify({"topic": topic, "result": result})
    except Exception as exc:
        return jsonify({"error": str(exc)}), 500


@app.route("/api/qna", methods=["POST"])
def qna():
    data = request.get_json(silent=True) or {}
    question = (data.get("question") or "").strip()
    context = (data.get("context") or "").strip()
    if not question:
        return jsonify({"error": "Question is required."}), 400
    try:
        result = answer_question(question, context)
        return jsonify({"question": question, "result": result})
    except Exception as exc:
        return jsonify({"error": str(exc)}), 500


@app.route("/api/summary", methods=["POST"])
def summary():
    data = request.get_json(silent=True) or {}
    content = (data.get("content") or "").strip()
    if not content:
        return jsonify({"error": "Content is required."}), 400
    try:
        result = summarize_content(content)
        return jsonify({"result": result})
    except Exception as exc:
        return jsonify({"error": str(exc)}), 500


if __name__ == "__main__":
    app.run(debug=Config.DEBUG, host="0.0.0.0", port=5000)
