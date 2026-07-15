# EduGenie

### AI-Powered Personalized Learning Platform using Google Gemini

![Python](https://img.shields.io/badge/Python-3.10+-blue)
![Flask](https://img.shields.io/badge/Flask-3.x-green)
![Google Gemini](https://img.shields.io/badge/Google-Gemini-orange)
![License](https://img.shields.io/badge/License-MIT-red)
![Status](https://img.shields.io/badge/Project-Completed-success)

---

# 📖 Overview

EduGenie is an AI-powered educational assistant developed as part of the **SmartBridge AI Virtual Internship Program**.

The platform leverages **Google Gemini AI** to provide intelligent educational assistance through AI-powered concept explanations, question answering, quiz generation, text summarization, and personalized learning paths.

EduGenie is designed to simplify learning, improve student engagement, and provide an interactive AI-based educational experience using modern Generative AI technologies.

---

# ✨ Features

- 📘 AI-Powered Concept Explanation
- ❓ Intelligent Question Answering
- 📝 AI Quiz Generation
- 📚 Smart Text Summarization
- 🎯 Personalized Learning Path Generator
- 🤖 Google Gemini AI Integration
- ⚡ Fast Response Generation
- 🎨 Responsive Web Interface
- 🔒 Secure API Key Management
- 📄 Modular Project Architecture

---

# 🛠 Technology Stack

| Category | Technology |
|-----------|------------|
| Programming Language | Python 3.10+ |
| Backend Framework | Flask |
| Frontend | HTML5, CSS3, JavaScript |
| Artificial Intelligence | Google Gemini API |
| Environment Management | python-dotenv |
| Testing | pytest |
| Version Control | Git & GitHub |
| IDE | Visual Studio Code |

---

# 🏗 System Architecture

```
                    User

                      │

                      ▼

        HTML • CSS • JavaScript

                      │

                      ▼

               Flask Backend

                      │

     ┌────────────┬────────────┐
     │            │            │
     ▼            ▼            ▼

 Explanation    Quiz      Learning Path

     │            │            │

     └───────┬────┴────────────┘
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
│   ├── screenshots/
│   │   ├── Explain.png
│   │   ├── HomePage.png
│   │   ├── Learning_Path.png
│   │   ├── QnA.png
│   │   └── Quiz.png
│   │
│   ├── EduGenie_Demo.mp4
│   └── logo.png
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
├── .gitignore
├── CHANGELOG.md
├── CODE_OF_CONDUCT.md
├── CONTRIBUTING.md
├── FEATURES.md
├── FUTURE_SCOPE.md
├── LICENSE
├── PROJECT_STRUCTURE.md
├── README.md
├── SECURITY.md
└── requirements.txt
```

---

# ⚙ Installation

## 1. Clone the Repository

```bash
git clone https://github.com/pranathiparimi3108/EduGenie.git

cd EduGenie
```

---

## 2. Create a Virtual Environment

### Windows

```bash
python -m venv venv

venv\Scripts\activate
```

### Linux/macOS

```bash
python3 -m venv venv

source venv/bin/activate
```

---

## 3. Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 4. Configure Environment Variables

Copy the example environment file.

### Windows

```bash
copy .env.example .env
```

### Linux/macOS

```bash
cp .env.example .env
```

Open the `.env` file and add your Gemini API key.

```env
GEMINI_API_KEY=YOUR_GEMINI_API_KEY
```

---

## 5. Run the Application

```bash
cd backend

python app.py
```

Open your browser:

```
http://127.0.0.1:5000
```

---

# 🧠 AI Modules

### 📘 Concept Explanation

Provides simple, detailed, and AI-generated explanations for educational topics.

---

### ❓ Question Answering

Allows students to ask questions and receive intelligent answers using Google Gemini.

---

### 📝 Quiz Generator

Generates multiple-choice quizzes with answers and explanations.

---

### 📚 Smart Summary

Converts lengthy study materials into concise revision notes.

---

### 🎯 Personalized Learning Path

Creates customized study plans based on the selected learning topic.

---

# 🌐 API Endpoints

| Method | Endpoint | Description |
|---------|----------|-------------|
| GET | `/api/health` | Health Check |
| POST | `/api/explain` | Explain a Topic |
| POST | `/api/qna` | Question Answering |
| POST | `/api/quiz` | Generate Quiz |
| POST | `/api/summary` | Summarize Content |
| POST | `/api/learning-path` | Generate Learning Path |

For complete API documentation, refer to:

```
docs/API_DOCUMENTATION.md
```

---

# 🖼 Screenshots

Application screenshots are available in the **assets/screenshots/** folder.

The repository includes screenshots of:

- 🏠 Home Page
- 📘 Concept Explanation
- ❓ Question Answering
- 📝 Quiz Generation
- 🎯 Personalized Learning Path

---

# 🎥 Demo Video

The complete project demonstration video is available in the **assets** folder.

**▶ [Download EduGenie Demo Video](assets/EduGenie_Demo.mp4)**

Watch the complete demo here:

[https://youtu.be/YOUR_VIDEO_ID](https://youtu.be/E1PSeyLu2P4)
---

# 🧪 Testing

Run the test suite:

```bash
cd backend

pytest tests
```

Testing includes:

- AI Module Integration
- API Validation
- Backend Functionality
- Error Handling
- User Input Validation

---

# 📚 Documentation

Complete documentation is available in the **docs/** directory.

- API Documentation
- Installation Guide
- User Guide
- SmartBridge Checklist

---

# 🔒 Security

This project follows secure development practices.

- API keys are stored using environment variables.
- `.env` files are excluded from version control.
- Sensitive credentials are never committed to GitHub.
- User inputs are validated before processing.

For more details, see **SECURITY.md**.

---

# 🚀 Future Enhancements

- User Authentication
- Student Dashboard
- Learning Progress Tracking
- PDF Upload and AI Analysis
- Voice Assistant Integration
- Multi-language Support
- Mobile Application
- Offline AI Model Support
- Cloud Deployment

---

# 🎯 Learning Outcomes

This project provided practical experience in:

- Generative AI
- Prompt Engineering
- Google Gemini API Integration
- Flask Web Development
- REST API Development
- Natural Language Processing (NLP)
- Software Documentation
- Git & GitHub

---

# 🤝 Contributing

Contributions are welcome.

1. Fork this repository.
2. Create a feature branch.
3. Commit your changes.
4. Push your branch.
5. Open a Pull Request.

Please read **CONTRIBUTING.md** before contributing.

---

# 👩‍💻 Author

**Parimi Venkata Pranathi**

B.Tech – Data Science

Vignan's Nirula Institute of Technology and Science for Women

GitHub: https://github.com/pranathiparimi3108

---

# 🙏 Acknowledgement

This project was developed as part of the **SmartBridge AI Virtual Internship Program**.

Special thanks to:

- SmartBridge
- Vignan's Nirula Institute of Technology and Science for Women
- Faculty Mentors
- Google Gemini AI

for their guidance and support throughout the project.

---

# 📄 License

This project is licensed under the **MIT License**.

See the **LICENSE** file for complete details.

---

⭐ **If you found this project useful, consider giving it a Star on GitHub!**
