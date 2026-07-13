# Installation Guide

## Prerequisites

- Python 3.10 or higher
- Google Gemini API key

## Setup

1. Clone the repository:

```bash
git clone https://github.com/pranathiparimi3108/EduGenie.git
cd EduGenie
```

2. Create and activate a virtual environment:

```bash
python -m venv venv
# Windows
venv\Scripts\activate
# macOS/Linux
source venv/bin/activate
```

3. Install dependencies:

```bash
pip install -r requirements.txt
```

4. Configure environment variables:

```bash
copy .env.example .env
```

Edit `.env` and add your `GEMINI_API_KEY`.

5. Run the application:

```bash
cd backend
python app.py
```

6. Open in browser:

```
http://127.0.0.1:5000
```

## Run tests

```bash
cd backend
pytest tests
```
