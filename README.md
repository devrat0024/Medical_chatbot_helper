 Dental Assistant Chatbot Web App
This is a simple, modern dental assistant chatbot web application that allows users to interact with a bot for booking appointments. The chatbot handles conversational form-filling and stores appointment data using MongoDB. A beautifully designed frontend built with Tailwind CSS enhances the user experience.

Project Structure
bash
Copy
Edit
Dental Chatbot Project
├── app.py                  # Flask backend handling chatbot logic and MongoDB
├── demo.html               # Main chatbot interface
├── index.html              # Landing page for clinic services and static booking form
├── dentist_17714361.png    # Dentist icon used in UI
├── download (6).jfif       # Background image for the web UI
 Features
 Chatbot for dental appointment booking.

 Captures name, date, time, age, and gender in a conversational flow.

 Frontend includes both chatbot UI and a modern landing page for services.

 Stores appointment data in a local MongoDB database.
 
 Responsive design with Tailwind CSS.

Session memory to handle conversational context.

 Getting Started
 Prerequisites
Python 3.x

MongoDB running locally (mongodb://localhost:27017)

Flask

Flask-CORS

pymongo

Install dependencies:

bash
Copy
Edit
pip install flask flask-cors pymongo
Run the App
Make sure MongoDB is running locally.

Start the Flask server:

bash
Copy
Edit
python app.py
Open demo.html in a browser (or use Flask templating to serve it).

Interact with the chatbot to book appointments.

 How it Works
The chatbot listens at /chat for incoming POST requests.

It handles a conversation flow to collect user data (like name, date, time, age, gender).

After collecting all data, it stores the information in MongoDB under dental_chatbot > appointments.

The frontend sends messages to the server and displays responses dynamically.
