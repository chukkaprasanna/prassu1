from flask import Flask, render_template, request, redirect, url_for, jsonify
import json
from datetime import datetime

app = Flask(__name__)

DATA_FILE = 'data.json'

# Load data
def load_data():
    try:
        with open(DATA_FILE, 'r') as file:
            return json.load(file)
    except:
        return []

# Save data
def save_data(data):
    with open(DATA_FILE, 'w') as file:
        json.dump(data, file, indent=4)

@app.route('/')
def welcome():
    return render_template('welcome.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        return redirect(url_for('home'))
    return render_template('login.html')

@app.route('/home')
def home():
    return render_template('home.html')

@app.route('/add_medication', methods=['GET', 'POST'])
def add_medication():
    if request.method == 'POST':
        new_med = {
            "name": request.form['med_name'],
            "dosage": request.form['dosage'],
            "frequency": request.form['frequency'],
            "start_date": request.form['start_date'],
            "end_date": request.form['end_date'],
            "morning_time": request.form['morning_time'],
            "afternoon_time": request.form['afternoon_time'],
            "night_time": request.form['night_time']
        }
        data = load_data()
        data.append(new_med)
        save_data(data)
        return redirect(url_for('home'))
    return render_template('add_medication.html')

@app.route('/view_medications')
def view_medications():
    data = load_data()
    return jsonify(data)

if __name__ == '__main__':
    app.run(debug=True)
