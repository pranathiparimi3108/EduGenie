# EduGenie

[![Python](https://img.shields.io/badge/Python-3.10+-blue.svg)](https://www.python.org/)
[![Flask](https://img.shields.io/badge/Flask-3.0+-black.svg)](https://flask.palletsprojects.com/)
[![Gemini AI](https://img.shields.io/badge/Gemini-AI-orange.svg)](https://ai.google.dev/)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)

**EduGenie** is an AI-powered personalized learning platform built with **Flask**, **Python**, and **Google Gemini AI**. It helps students learn faster through intelligent explanations, personalized learning paths, AI-generated quizzes, summaries, and interactive Q&A.

> Built by **Parimi Venkata Pranathi**  
> Vignan's Nirula Institute of Technology and Science for Women

---

## Features

- **Topic Explanation** — Learn any concept in simple language
- **Personalized Learning Path** — Day-by-day study plans
- **AI Quiz Generator** — MCQs with answers and explanations
- **Interactive Q&A** — Ask doubts and get instant help
- **Smart Summaries** — Turn long notes into revision bullets

---

## Tech Stack

| Layer | Technology |
|-------|------------|
| Backend | Python, Flask |
| AI | Google Gemini API |
| Frontend | HTML, CSS, JavaScript |
| Testing | pytest |
| Config | python-dotenv |

---

## Project Structure

```
EduGenie/
├── backend/
│   ├── ai/              # Gemini integration
│   ├── modules/         # Feature modules
│   ├── static/          # Web UI
│   ├── tests/           # Test suite
│   └── app.py           # Flask entry point
├── assets/              # Screenshots, logo, demo
├── docs/                # Documentation
└── README.md
```

See [PROJECT_STRUCTURE.md](PROJECT_STRUCTURE.md) for details.

---

## Installation

### 1. Clone the repository

```bash
git clone https://github.com/pranathiparimi3108/EduGenie.git
cd EduGenie
```

### 2. Create virtual environment

```bash
python -m venv venv
venv\Scripts\activate        # Windows
# source venv/bin/activate   # macOS/Linux
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure environment

```bash
copy .env.example .env
```

Add your Gemini API key to `.env`:

```
GEMINI_API_KEY=your_api_key_here
```

### 5. Run the app

```bash
cd backend
python app.py
```

Open: **http://127.0.0.1:5000**

---

## API Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/api/health` | Health check |
| POST | `/api/explain` | Explain a topic |
| POST | `/api/learning-path` | Generate learning path |
| POST | `/api/quiz` | Generate quiz |
| POST | `/api/qna` | Answer a question |
| POST | `/api/summary` | Summarize content |

Full docs: [docs/API_DOCUMENTATION.md](docs/API_DOCUMENTATION.md)

---

## Run Tests

```bash
cd backend
pytest tests
```

---

## Screenshots

> Add screenshots to `assets/screenshots/` and update this section.

| Home | Quiz | Learning Path |
|------|------|---------------|
| Coming soon | Coming soon | Coming soon |

---

## SmartBridge Submission

This project is prepared for SmartBridge evaluation with:

- Modular AI architecture
- Complete documentation
- GitHub-ready structure
- Test suite

Checklist: [docs/SMARTBRIDGE_CHECKLIST.md](docs/SMARTBRIDGE_CHECKLIST.md)

---

## Future Enhancements

- User authentication
- Progress tracking
- PDF notes export
- Voice input / text-to-speech
- Deployment with live demo

See [FUTURE_SCOPE.md](FUTURE_SCOPE.md)

---

## Author

**Parimi Venkata Pranathi**  
Data Science Student | AI Enthusiast  
Vignan's Nirula Institute of Technology and Science for Women  
GitHub: [@pranathiparimi3108](https://github.com/pranathiparimi3108)

---

## License

This project is licensed under the MIT License. See [LICENSE](LICENSE).
