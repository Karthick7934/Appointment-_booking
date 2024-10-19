**Appointment Booking Chatbot using Flask, OpenAI GPT, and MySQL**
**Project Overview**
This project is a chatbot application designed to help users book appointments. The chatbot uses OpenAI GPT-3.5 to interact with users and MySQL to store user data and appointment details. The backend is built using Python's Flask framework, and the frontend uses HTML and CSS to provide a simple user interface for the booking process.

**Features**
    NLP-based chatbot powered by OpenAI GPT-3.5 (ChatGPT model) to handle user interaction.
    Appointment booking system: The bot collects user details such as name, email, phone number, and age.
    Database integration using MySQL to store appointment data and retrieve available slots.
    Flask-based web interface to interact with the chatbot.
    User-friendly interface for selecting available appointment slots.
Tech Stack
    Backend: Python (Flask framework)
    Database: MySQL
    NLP/AI: OpenAI GPT-3.5 (using the OpenAI API)
    Frontend: HTML5, CSS3 (no JavaScript)
    Hosting: Flask runs locally or can be deployed on cloud platforms.
**Project Structure**
        appointment-booking/
        │
        ├── templates/
        │   ├── index.html     # Main UI for the appointment system
        ├── static/
        │   ├── style.css      # CSS file for styling the UI
        ├── app.py             # Flask app containing backend logic
        ├── Dockerfile         # Docker configuration file
        ├── requirements.txt   # Python dependencies
        └── README.md          # Project README file (this file)

**Step-by-Step Guide**
**1. Clone the Repository \n **
    git clone <repository-url>
    cd appointment-booking
**2. Install Dependencies**
    Create and activate a virtual environment:
    python -m venv venv
    source venv/bin/activate  # On Windows: venv\Scripts\activate
Install required Python packages:
pip install -r requirements.txt
**3. Set Up MySQL Database**
Create a MySQL database named appointment_db and create a table:
CREATE DATABASE appointment_db;
USE appointment_db;
CREATE TABLE appointments (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255),
    email VARCHAR(255),
    phone_number VARCHAR(20),
    age INT,
    appointment_time DATETIME
);
**4. Configure OpenAI API Key**
        Set up your OpenAI API key in the app.py file: openai.api_key = 'YOUR_OPENAI_API_KEY'
        Alternatively, you can set it as an environment variable.
**5. Run the Flask Application**
Start the Flask development server:python app.py

