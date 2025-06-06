# Xeno Version1 – AI Style Chatbot – Backend Focused Full Stack Application

## Overview
A minimalist, full-stack AI chatbot project built using **Flask** (Python) and **SentenceTransformer(Mini AI Model)** on the backend and **HTML + JavaScript** on the frontend. It supports REST API, and a styled frontend that simulates AI response typing.

## Live Demo
[View Live App](https://xenochatbot-production.up.railway.app/)

## Tech Stack
Python, Flask, Javascript, OOP, HTML, CSS, Railway, SentenceTransformer, templates, Docker, Util, Mini AI Model

## Features
### Smart NLP Input Parsing
- Supports natural language queries like "add five and twenty" or "bitwise xor of 5 and 9".
- Automatically converts number words to digits using word2number.

### Semantic & Symbolic Operator Recognition
- Detects and evaluates both keywords (add, power, bitwise xor) and symbols (+, **, ^).
- Handles mathematical and bitwise operations intelligently.

### Safe Expression Evaluation with numexpr
- Supports direct expression inputs like 2*3+5/2 using optimized evaluation.
- Includes fallback logic for operator-based expressions.

### Bitwise Operation Support
- Supports AND, XOR, NOT, LEFT SHIFT, RIGHT SHIFT with various input styles.
- Recognizes multiple keyword variations like "bitwise xor", "<<", "right shift", etc.

### Timezone-Aware Date & Time Handling
- Returns Indian date/time (Asia/Kolkata) regardless of server location.
- Commands like "get current time" or "get date and time" return localized output.

### Semantic Intent Matching with Sentence Transformers
- Uses sentence-transformers (MiniLM) for best-fit query matching.
- Handles topics like Windows, Linux, GitHub, PowerShell, MySQL, and computer science concepts.

### Fallback to Basic Assistant Mode
- Provides predefined assistant responses when semantic intent match is weak.
- Responds with friendly prompts and guidance messages.

### Expandable Command Dictionary
- Command database easily extendable and organized by category (windows_cmds, news_queries, etc.).

### Offline Ready
- Once installed on your desktop, the chatbot runs completely offline using a lightweight Mini LLM model. All responses are served from a local dictionary — no external API calls required (except optional Google News API for live news).

## Additional Highlights
- Modular, production-ready backend-focused AI-style chatbot built with Python and Flask REST API.
- Integrated Google News API for live news fetching.
- Utilizes Flask blueprints, decorators, and factory pattern for clean project structure.
- Frontend implemented with HTML, CSS, and JavaScript for interactive UI.
- Uses lightweight MiniLM model from SentenceTransformer for semantic NLP.
- Deployed with Docker and Railway, managing secure environment variables.
- CI/CD workflow enabled with automated GitHub pushes.

## Getting Started (Local Setup)
### 1. Clone the repo
```bash
git clone https://github.com/Ethertyson/xeno_chatbot.git
cd xeno_chatbot
```

### 2. Set up virtual environment
```bash
python -m venv venv
source venv/bin/activate   # or venv\Scripts\activate on Windows
pip install -r requirements.txt # To install dependencies
```

### 3. Setup environment variables (.env file):
Create a .env file in the root directory with the following variables:
- FLASK_ENV=development
- GOOGLE_NEWS_API_KEY=your_key
- GOOGLE_NEWS_API_HOST=google_news_api_host

### 4. Run the app locally:
```bash
flask run	# OR python run.py
```

## Docker
Build and run the Docker image:
```bash
docker build -t xeno-chatbot .  # Build
docker run -p 5000:5000 xeno-chatbot  # Run
```
## Deployment
Deployed on Railway: https://xenochatbot-production.up.railway.app/

## Deploy at your end
- Push your code to GitHub
- Connect your repo to Railway (or any other cloud platform)
- Add required environment variables in Railway settings
- Deploy and access your live URL

## API Documentation
API Endpoint: /chatAiModel  # Http Method should be POST
### Example1:
#### INPUT
```json
{
  "Message":"Tell me the command to make directory in windows."
}
```
#### OUTPUT    # Status Code 200 OK
```json
{
  "Status":"Success",
  "Message":"mkdir DIRECTORY_NAME"
}
```
### Example2:
#### INPUT
```json
{
  "Message":"Hi"
}
```
#### OUTPUT    # Status Code 200 OK
```json
{
  "Status":"Success",
  "Message":"Hello! How can I help you today?"
}
```

## Project Architecture
- chatbot_api        # root directory
- chatbot_api/run.py
- chatbot_api/venv
- chatbot_api/.gitignore
- chatbot_api/.env
- chatbot_api/config.py
- chatbot_api/.dockerignore
- chatbot_api/Dockerfile
- chatbot_api/requirements.txt
- chatbot_api/app/models
- chatbot_api/app/routes
- chatbot_api/app/static
- chatbot_api/app/templates
- chatbot_api/app/utils
- chatbot_api/app/__init__.py
- chatbot_api/app/extension.py

## License
This project is licensed under the MIT License — meaning you’re free to use, modify, and distribute the code with proper credit. The software is provided “as is” without any warranty. Feel free to use this chatbot offline or integrate it into your own projects!

## Note
This is an independent project licensed under MIT. Not affiliated with any existing product or brand named ‘Xeno’.

## Author
Pritanshu Srivastava | pritanshusrivastava24880@gmail.com | [LinkedIn](https://www.linkedin.com/in/pritanshu-srivastava-59aaa7226/) | [HackerRank](hackerrank.com/profile/pritanshusrivas1)
