# 🐦 Twitter Mentions Service

A Python-based FastAPI microservice that fetches tweet mentions of a given Twitter user using the [TwitterAPI.io](https://docs.twitterapi.io) API.  
It returns a list of `tweet_ids` in which the user is mentioned, with support for logging and CLI-based testing.

---

## ✨ Features

- Fetch latest tweet mentions of any user (by `userName`)
- Returns tweet IDs only (lightweight and fast)
- Proper modular structure with FastAPI routing
- Logging support to track API usage and failures
- Command-line test runner via `app.py`
- RESTful endpoint with Swagger docs for easy testing

---

## 🧱 Prerequisites

- Python 3.10+
- Virtual Environment (recommended)
- API Key from [TwitterAPI.io](https://docs.twitterapi.io)

---

## 📁 Project Structure

```bash
twitter-mentions-service/
├── api/
│   └── twitter_mentions_service_api.py      # FastAPI app
├── src/
│   ├── components/
│   │   └── twitter_mentions_service.py      # Core logic to fetch mentions
│   └── logging/
│       └── __init__.py                      # Logging configuration
├── logs/                                    # Auto-created log files
├── app.py                                   # Test script to run from CLI
├── .env.prod                                # Stores the API key
├── requirements.txt                         # Python dependencies
└── README.md                                # Project documentation
```

---

## 🧰 Installation

1. **Clone the repository**:
   ```bash
   git clone <repository-url>
   cd twitter-mentions-service
   ```

2. **Create and activate a virtual environment** (recommended):
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: .\venv\Scripts\activate
   ```

3. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Environment Variables**:
   - Create a `.env.prod` file in the root directory
   - Add the following environment variable:
     ```env
     X_API_KEY=your_api_key_here
     ```

---

## 🚀 Running the Service

### 1. Running the API Server

The API server provides a RESTful endpoint to fetch mentions. To start the server:

```bash
uvicorn api.twitter_mentions_service_api:app --reload
```

This will start the server at `http://localhost:8000` with the following endpoint:

- **GET** `/mentions?userName={user}`
  - Returns the list of tweet IDs where the user was mentioned

### 2. Running the Test Application

The test application (`app.py`) provides a command-line interface to test the mention fetching service:

```bash
python app.py
```

---

## 📥 API Response Format

### ✅ Example Request:

```http
GET /mentions?userName=id_bachao
```

### ✅ Sample Response:

```json
{
  "mention": "id_bachao",
  "tweet_ids": [
    "1891173800697278487",
    "1891173690504597847"
  ]
}
```

### Response Fields Explanation

- `mention`: The Twitter user screen name
- `tweet_ids`: List of tweet IDs where the user was mentioned

---

## 🧾 Logs

Logs are stored in the `logs/` folder and named by timestamp, like:

```
logs/log_2025-03-24_09-30-55.log
```

Each log entry records:
- API requests and success responses
- Errors and exception messages

---

## 🚫 Error Handling

| Code | Meaning                   | Cause                           |
|------|----------------------------|----------------------------------|
| 400  | Bad Request               | Missing or invalid `userName`   |
| 401  | Unauthorized              | Invalid API key                 |
| 500  | Internal Server Error     | Failed to fetch or parse data   |

---

## 🤝 Contributing

Contributions are welcome!  
If you find bugs or want to add enhancements, feel free to open a PR or issue.

---

## 📜 License

This project is licensed under the MIT License.  
See the [LICENSE](LICENSE) file for details.

---

