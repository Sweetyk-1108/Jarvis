# J.A.R.V.I.S.  (Just A Rather Very Intelligent System)

# 🤖 Jarvis AI Assistant

Jarvis is a Python-based AI voice assistant. It can perform various tasks using voice commands and automation features.

## Source Code :

https://github.com/Sweetyk-1108/Jarvis.git

## ✨ Features

- 🎤 Voice command recognition
- 🔊 Text-to-speech responses
- 🌐 Open websites using voice commands
- 🕒 Tell date and time
- 🔍 Search information on the internet
- 📂 Open applications and files
- 💬 Interactive conversations
- ⚡ Easy to customize and extend

## 🛠️ Technologies Used

- Python
- SpeechRecognition
- Django
- HTML/CSS
- Wikipedia API
- VS Code

## 📁 Project Structure

Jarvis/
│
├── Jarvis/                         # <-- Main Django Application Directory
│   ├── jarvis/                     # Django App containing logic, models, and views
│   │   ├── migrations/
│   │   ├── models.py               # ChatHistory database model
│   │   ├── urls.py
│   │   └── views.py                # Main request logic & Groq API client integration
│   │
│   ├── jarvis_project/             # Django Project Configuration
│   │   ├── settings.py
│   │   └── urls.py
│   │
│   ├── templates/
│   │   └── index.html              # Frontend UI with Speech API integration
│   │
│   ├── .env                        # Local environment credentials (API Key)
│   ├── db.sqlite3                  # Local database
│   └── manage.py                   # Django CLI utility
│
├── venv/                           # Virtual Environment
└── manage.py                       
