from flask import Flask, render_template, request, jsonify
from flask_cors import CORS
from pymongo import MongoClient
from uuid import uuid4

app = Flask(__name__)
CORS(app)

client = MongoClient("mongodb://localhost:27017")
db = client['dental_chatbot']
collection = db['appointments']

# Session memory to simulate context
session_memory = {}

@app.route('/')
def home():
    return render_template('demo.html')

@app.route('/chat', methods=['POST'])
def chat():
    data = request.get_json()
    msg = data.get("message", "").lower()
    session_id = data.get("sessionId") or str(uuid4())

    memory = session_memory.setdefault(session_id, {})

    # Chat flow for appointment booking
    if 'appointment' in msg:
        memory['stage'] = 'ask_name'
        return jsonify(reply="Great! What's the patient's name?", sessionId=session_id)

    elif memory.get('stage') == 'ask_name':
        memory['name'] = msg.title()
        memory['stage'] = 'ask_date'
        return jsonify(reply="Thanks! What's the appointment date (YYYY-MM-DD)?", sessionId=session_id)

    elif memory.get('stage') == 'ask_date':
        memory['date'] = msg
        memory['stage'] = 'ask_time'
        return jsonify(reply="Noted. What time do you prefer?", sessionId=session_id)

    elif memory.get('stage') == 'ask_time':
        memory['time'] = msg
        memory['stage'] = 'ask_age'
        return jsonify(reply="Please provide the patient's age.", sessionId=session_id)

    elif memory.get('stage') == 'ask_age':
        memory['age'] = msg
        memory['stage'] = 'ask_gender'
        return jsonify(reply="And what's the gender (male/female/other)?", sessionId=session_id)

    elif memory.get('stage') == 'ask_gender':
        memory['gender'] = msg.capitalize()

        appointment = {
            "_id": str(uuid4()),
            "name": memory['name'],
            "date": memory['date'],
            "time": memory['time'],
            "age_id": memory['age'],
            "gender_id": memory['gender']
        }

        collection.insert_one(appointment)
        session_memory.pop(session_id)

        return jsonify(reply=f"✅ Appointment booked for {appointment['name']} on {appointment['date']} at {appointment['time']}.", sessionId=session_id)

    return jsonify(reply="Hi! I can help you book dental appointments. How may I help you today?", sessionId=session_id)

if __name__ == '__main__':
    app.run(debug=True)
