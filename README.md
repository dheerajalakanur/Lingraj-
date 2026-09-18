# Darukaa.Earth AI Biodiversity Chatbot

This project is a basic implementation of the AI Biodiversity Intelligence Chatbot Challenge. It includes a frontend built with React (via CDN) and a backend built with Python (FastAPI).

## Project Structure (Vercel Ready!)
- `public/`: Contains the UI written in HTML, CSS, and React (app.jsx). It runs directly in the browser without needing a Node.js build step.
- `api/`: Contains the Python FastAPI server that acts as the backend and includes a mock knowledge base simulating RAG (Retrieval-Augmented Generation) and environmental reasoning.
- `vercel.json`: Configuration file to instantly deploy both the frontend and Python backend to Vercel as one app.

## How to Deploy to Vercel (Free & Permanent)

This project is already pre-configured to be deployed on Vercel without any modifications!

1. **Upload to GitHub**:
   - Initialize a git repository in this folder and push it to a new public or private repository on your GitHub account.
2. **Deploy on Vercel**:
   - Go to [Vercel.com](https://vercel.com/) and log in with your GitHub account.
   - Click **"Add New..." -> "Project"**.
   - Import the repository you just created.
   - Leave all the default settings (Vercel will automatically detect `vercel.json`).
   - Click **Deploy**! 

Within 1-2 minutes, Vercel will give you a live, permanent public HTTPS link for your chatbot.

## How to Run Locally

### 1. Start the Backend Server
Open a terminal, navigate to the `api` folder, and run:
```bash
cd api
pip install -r requirements.txt
python index.py
```
The backend API will start on `http://localhost:8000`.

### 2. Start the Frontend
Since the frontend is pure HTML/JS, you can simply open `public/index.html` in your web browser. 

Alternatively, if you have Python installed, you can serve it via a simple HTTP server:
```bash
cd public
python -m http.server 3000
```
Then navigate to `http://localhost:3000` in your browser.

## Features Included
- **Knowledge System:** Uses a mock structured dataset representing a knowledge base (in `knowledge_base.py`).
- **Conversational Intelligence:** Can ask for more context if input is too short.
- **Evidence-Backed Recommendations:** Responses include actionable recommendations, scientific reasoning, impacted metrics, time horizons, confidence levels, and references as requested in the challenge.
- **Multilingual Support:** Seamlessly switch between English, Hindi, and Kannada.
