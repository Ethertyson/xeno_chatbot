 
# Xeno Version1 – AI Style Chatbot – Backend Focused Full Stack Application

## Overview
A minimalist, full-stack AI chatbot project built using **Flask** (Python) and **SentenceTransformer(Mini AI Model)** on the backend and **HTML + JavaScript** on the frontend. It supports REST API, and a styled frontend that simulates AI response typing.

## Live Demo
[View Live App](https://xenochatbot-production.up.railway.app/)

## Tech Stack
Python, Flask, Javascript, OOP, HTML, CSS, Railway, SentenceTransformer, templates, Docker, Util, AI Model

## Features
- Built a modular, production-ready, and backend focused full stack AI Style Chatbot using Python and Flask REST API.
- Pushed code to GitHub for automated deployment enabling smooth CI/CD flow. Integrated Google News API.
- Implemented blueprints, decorators, factory patterns, and templates for interactive UI using HTML, CSS, and Javascript.
- Used mini AI model from SentenceTransformer for semantic matches. Implemented Rule based logic.
- Created virtual environment, dockerized and deployed on Railway with secure environment variable management.

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

## Project Structure
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

## Author
Pritanshu Srivastava | pritanshusrivastava24880@gmail.com | [LinkedIn](https://www.linkedin.com/in/pritanshu-srivastava-59aaa7226/) | [HackerRank](hackerrank.com/profile/pritanshusrivas1)
