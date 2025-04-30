# AI Calendar Assistant 📅

An intelligent desktop assistant that helps you generate and schedule calendar events using natural language prompts. It integrates ChatGPT for interpreting text and Google Calendar APIs for event creation. Comes with a simple GUI for user interaction.

---

## 🚀 Features

- 🗨️ Accepts natural language input (e.g., "Math class next Friday at 1 PM")
- 🤖 Uses ChatGPT to parse and extract event details
- 📅 Automatically creates events in your Google Calendar
- 🖥️ Lightweight desktop GUI interface

---

## 🛠 Tech Stack

- Python 3
- Tkinter (GUI)
- OpenAI API (ChatGPT)
- Google Calendar API 
- Speach Recognition (PyAudio)

---

## 📦 Installation

1. **Clone the repo**

    ```bash
    git clone https://github.com/Vimpel-O-O/AiCalendar.git

    cd AI_CALENDAR
    ```    

2. **Create a virtual environment (optional but recommended)**
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows: venv\Scripts\activate
    ```
3. **Install dependencies**
    ```bash
    pip install -r requirements.txt
    ```
4. **Get required API keys**
    - CHATGPT_API_KEY ([openai.com/api/](https://openai.com/api/))
    
    - GOOGLE_CREDENTIALS & GOOGLE_USER_TOKEN ([developers.google.com/workspace/calendar/api/quickstart/python](https://developers.google.com/workspace/calendar/api/quickstart/python))
    
    - CALENDAR_ID
        - Go to calendar settings in Google Calendar and scroll to Calendar ID

5. **Create .env and add API keys**
    ```bash
    CHATGPT_API_KEY = your_key_here
    GOOGLE_CREDENTIALS = your_credentials.json
    GOOGLE_USER_TOKEN = your_google_user_token
    CALENDAR_ID = your_calendar_id
    ```

6. **▶️ Running the App**
    ```bash
    python run.py
    ```

## 🎥 Demo

[![Watch the video](https://img.youtube.com/vi/VIDEO_ID/0.jpg)](https://www.youtube.com/watch?v=VIDEO_ID)



