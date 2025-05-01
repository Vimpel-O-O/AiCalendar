# AI Calendar Assistant 📅

A useful desktop assistant application that helps you generate and schedule calendar events using natural language prompts. It integrates ChatGPT for interpreting text and Google Calendar APIs for event creation. Comes with a simple GUI for user interaction.

With this program, I was able to save a lot of time keeping my calendar up to date and boost my productivity by reducing recurring manual work and giving more attention to the schedule structure itself.

---

## 🚀 Features

- 🗨️ Accepts natural language input (e.g., "Book a meeting with Sarah next Monday at 10 AM")
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
        - Go to calendar settings in Google Calendar and scroll to Calendar ID. In my case I used 4 calendar types for personal use - "SWE related", "College related", "Work related" and "Other". (Edit "# Set the event type" section code in main.py, line 66, accordingly)

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

[![Watch the video](https://img.youtube.com/vi/Iq5E-pjKnmw/0.jpg)](https://www.youtube.com/watch?v=Iq5E-pjKnmw)

## 💡 Use cases to try
- 🎓 "Math class next Friday at 1 PM"
- 💼 "Standup meeting at work from 9AM to 10:30AM on Tuesday"
- 👨‍💻 "Do leetcode practice at 6 to 8PM daily"
- 🏋️ "Workout session every Friday 5 to 6PM"
- 👥 "Weekly Computer Science club meetup at 3-4PM on Wednesday"



