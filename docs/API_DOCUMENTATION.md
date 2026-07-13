# API Documentation

Base URL: `http://127.0.0.1:5000`

## Health Check

**GET** `/api/health`

Response:
```json
{
  "status": "ok",
  "app": "EduGenie"
}
```

## Explain Topic

**POST** `/api/explain`

Body:
```json
{
  "topic": "Neural Networks",
  "level": "beginner"
}
```

## Learning Path

**POST** `/api/learning-path`

Body:
```json
{
  "topic": "Python",
  "duration_days": 7
}
```

## Quiz

**POST** `/api/quiz`

Body:
```json
{
  "topic": "Data Structures",
  "num_questions": 5
}
```

## Q&A

**POST** `/api/qna`

Body:
```json
{
  "question": "What is overfitting?",
  "context": "Machine Learning"
}
```

## Summary

**POST** `/api/summary`

Body:
```json
{
  "content": "Long study notes or chapter text..."
}
```

## Error format

```json
{
  "error": "Error message"
}
```
