# Project Structure

```
EduGenie/
├── backend/
│   ├── ai/                 # AI model integrations
│   ├── modules/            # Feature-specific business logic
│   ├── static/             # Frontend HTML, CSS, JS
│   ├── tests/              # Automated tests
│   ├── app.py              # Flask application entry point
│   ├── config.py           # Environment configuration
│   └── requirements.txt    # Backend dependencies
├── assets/
│   ├── screenshots/        # UI screenshots for README
│   ├── logo/               # Project logo
│   └── demo/               # Demo GIF or video
├── docs/                   # Documentation
├── .env.example            # Environment variable template
├── .gitignore
├── README.md
├── LICENSE
└── requirements.txt
```

## Module responsibilities

| Module | Purpose |
|--------|---------|
| `explanation.py` | Generate topic explanations |
| `learning_path.py` | Build personalized study plans |
| `quiz.py` | Generate MCQ quizzes |
| `qna.py` | Answer student questions |
| `summary.py` | Summarize study content |
