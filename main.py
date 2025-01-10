from flask import Flask, jsonify, render_template, redirect, request, url_for
import json
import os

app = Flask(__name__)
app.config['SECRET_KEY'] = 'CORINTHIANS'

DATA_FILE = 'data.json'

# Functions
def load_data():
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, "r") as file:
            return json.load(file)
    return []

def save_data(new_data):
    data = load_data()
    data.append(new_data) 
    with open(DATA_FILE, "w") as file:
        json.dump(data, file, indent=4)

# Routes
@app.route('/') 
def load():
    return render_template('load.html')
    # return render_template('test.html')    

@app.route('/intro')
def intro():
    return render_template("intro.html")

@app.route('/home')
def home():
    return render_template("home.html")

@app.route('/goals')
def goals():
    return render_template("goals.html")

@app.route('/data', methods=['GET'])
def get_data():
    return jsonify(load_data()), 200

@app.route('/userchange', methods=['POST']) 
def userchange():
    return render_template('load.html')

@app.route('/infochange', methods=['POST']) 
def infochange():
    return render_template('info.html')

@app.route('/save', methods=['POST'])
def save():
    data = request.json
    if not data:
        return jsonify({"error": "No data provided"}), 400
    
    save_data(data)
    return jsonify({"message": "Data saved successfully!"}), 200

@app.route('/login', methods=['POST'])
def login():
    if request.method == "POST":
        return render_template("start.html")
    return render_template("intro.html")

@app.route('/start', methods=['POST'])
def start():
    if request.method == "POST":
        return render_template("info.html")
    return render_template("start.html")

@app.route('/info', methods=['POST'])
def info():
    if request.method == "POST":
        return redirect(url_for('goals'))
    return render_template("info.html")

@app.route('/clearHistory', methods=['POST'])
def clear_history():
    filename = 'data.json' 
    try:
        if os.path.exists(filename):
            os.remove(filename)
            return render_template("load.html")
        else:
            return render_template("load.html")
    except Exception as e:
        return f"An error occurred: {e}"

if __name__ in "__main__":
    app.run(debug=True)

