<p align="center">
  <img src="assets/logo/logo.png" alt="EduGenie Logo" width="180">
</p>

<h1 align="center">EduGenie</h1>

<p align="center">
<b>AI-Powered Personalized Learning Platform using Google Gemini</b>
</p>

<p align="center">

![Python](https://img.shields.io/badge/Python-3.10+-blue)
![Flask](https://img.shields.io/badge/Flask-3.x-green)
![Google Gemini](https://img.shields.io/badge/Google-Gemini-orange)
![MIT License](https://img.shields.io/badge/License-MIT-red)
![Status](https://img.shields.io/badge/Project-Completed-success)

</p>

---

# 📖 Overview

EduGenie is an **AI-powered personalized learning platform** developed as part of the **SmartBridge AI Virtual Internship Program**.

The platform leverages **Google Gemini AI** to provide intelligent educational assistance by generating concept explanations, answering academic questions, creating quizzes, summarizing study materials, and generating personalized learning paths.

EduGenie aims to make learning more interactive, personalized, and efficient through the power of Generative AI.

---

# 📑 Table of Contents

- Overview
- Features
- Technology Stack
- Project Architecture
- Project Structure
- Installation
- API Endpoints
- Screenshots
- Demo Video
- Testing
- Documentation
- Security
- Future Enhancements
- Learning Outcomes
- Author
- Acknowledgement
- License

---

# ✨ Features

- 📘 AI-Powered Concept Explanation
- ❓ Intelligent Question Answering
- 📝 AI Quiz Generator
- 📚 Smart Text Summarization
- 🎯 Personalized Learning Path Generator
- 🤖 Google Gemini AI Integration
- ⚡ Fast Response Generation
- 🎨 Responsive User Interface
- 🔒 Secure API Key Management
- 📄 Modular Project Architecture

---

# 🛠 Technology Stack

| Layer | Technology |
|---------|------------|
| Programming Language | Python |
| Backend | Flask |
| Artificial Intelligence | Google Gemini API |
| Frontend | HTML5, CSS3, JavaScript |
| Environment | python-dotenv |
| Testing | pytest |
| Version Control | Git & GitHub |
| IDE | Visual Studio Code |

---

# 🏗 Project Architecture

```
                User

                  │

                  ▼

     HTML • CSS • JavaScript

                  │

                  ▼

            Flask Backend

                  │

       ┌──────────┼──────────┐
       │          │          │
       ▼          ▼          ▼

 Explanation    Quiz      Learning Path

       │          │          │

       └──────┬───┴──────────┘
              ▼

      Google Gemini AI

              │

              ▼

      AI Generated Response
```

---

# 📂 Project Structure

```
EduGenie/
│
├── assets/
│   ├── logo/
│   ├── screenshots/
│   └── demo/
│
├── backend/
│   ├── ai/
│   ├── modules/
│   ├── static/
│   ├── tests/
│   ├── app.py
│   ├── config.py
│   └── requirements.txt
│
├── docs/
│   ├── API_DOCUMENTATION.md
│   ├── INSTALLATION.md
│   ├── SMARTBRIDGE_CHECKLIST.md
│   └── USER_GUIDE.md
│
├── .env.example
├── README.md
├── LICENSE
├── SECURITY.md
├── CONTRIBUTING.md
├── CHANGELOG.md
└── requirements.txt
```

---

# ⚙ Installation

## 1️⃣ Clone the Repository

```bash
git clone https://github.com/pranathiparimi3108/EduGenie.git

cd EduGenie
```

---

## 2️⃣ Create a Virtual Environment

Windows

```bash
python -m venv venv

venv\Scripts\activate
```

Linux / macOS

```bash
python3 -m venv venv

source venv/bin/activate
```

---

## 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 4️⃣ Configure Environment Variables

Copy the example file.

Windows

```bash
copy .env.example .env
```

Linux / macOS

```bash
cp .env.example .env
```

Open `.env`

```env
GEMINI_API_KEY=YOUR_GEMINI_API_KEY
```

---

## 5️⃣ Run the Application

```bash
cd backend

python app.py
```

Open

```
http://127.0.0.1:5000
```

---

# 🧠 AI Modules

### 📘 Concept Explanation

Explains academic concepts in a simple and understandable manner.

---

### ❓ Question Answering

Answers educational questions using Google Gemini AI.

---

### 📝 Quiz Generator

Creates AI-generated multiple-choice questions with answers and explanations.

---

### 📚 Smart Summary

Converts lengthy study material into concise notes and revision points.

---

### 🎯 Personalized Learning Path

Generates structured study plans based on the selected topic.

---

# 🌐 API Endpoints

| Method | Endpoint | Description |
|---------|----------|-------------|
| GET | `/api/health` | Health Check |
| POST | `/api/explain` | Generate Explanation |
| POST | `/api/qna` | Answer Questions |
| POST | `/api/quiz` | Generate Quiz |
| POST | `/api/summary` | Generate Summary |
| POST | `/api/learning-path` | Generate Learning Path |

For detailed API documentation, see:

```
docs/API_DOCUMENTATION.md
```

---

# 🖼 Screenshots

## Home Page

![Home](assets/screenshots/home.png)

---

## Concept Explanation

![Explanation](assets/screenshots/explanation.png)

---

## Question Answering

![QnA](assets/screenshots/qna.png)

---

## Quiz Generation

![Quiz](assets/screenshots/quiz.png)

---

## Learning Path

![Learning Path](assets/screenshots/learning_path.png)

---

## Summary

![Summary](assets/screenshots/summary.png)

---

# 🎥 Demo Video

Watch the complete project demonstration.

**▶ [EduGenie Demo Video](assets/demo/EduGenie_Demo.mp4)**

---

# 🧪 Testing

Run all tests.

```bash
cd backend

pytest tests
```

The project includes testing for:

- AI module integration
- Backend functionality
- API response validation
- Error handling
- User input validation

---

# 📚 Documentation

Complete project documentation is available in the `docs/` folder.

- API Documentation
- Installation Guide
- User Guide
- SmartBridge Checklist

---

# 🔒 Security

This project follows standard security practices.

- API keys are stored using environment variables.
- `.env` files are excluded from GitHub.
- Sensitive credentials are never committed.
- User inputs are validated before processing.

For more information, refer to:

```
SECURITY.md
```

---

# 🚀 Future Enhancements

- User Authentication
- Student Dashboard
- Learning Progress Tracking
- PDF Upload & AI Analysis
- Voice Assistant
- Multi-language Support
- Mobile Application
- Offline AI Model Integration
- Cloud Deployment

---

# 🎯 Learning Outcomes

This project provided practical experience in:

- Generative AI
- Google Gemini API
- Prompt Engineering
- REST API Development
- Flask Web Development
- AI-Powered Educational Systems
- Natural Language Processing (NLP)
- Git & GitHub
- Software Documentation

---

# 🤝 Contributing

Contributions are welcome.

1. Fork the repository.
2. Create a feature branch.
3. Commit your changes.
4. Push the branch.
5. Open a Pull Request.

Please read **CONTRIBUTING.md** before contributing.

---

# 👩‍💻 Author

## Parimi Venkata Pranathi

**B.Tech – Data Science**

Vignan's Nirula Institute of Technology and Science for Women

GitHub:
https://github.com/pranathiparimi3108

---

# 🙏 Acknowledgement

This project was developed as part of the **SmartBridge AI Virtual Internship Program**.

Special thanks to:

- SmartBridge
- Vignan's Nirula Institute of Technology and Science for Women
- Faculty Mentors
- Google Gemini AI

for their continuous support and guidance throughout the project.

---

# 📄 License

This project is licensed under the **MIT License**.

See the **LICENSE** file for more details.

---

<p align="center">
⭐ If you found this project helpful, consider giving it a Star on GitHub!
</p>
