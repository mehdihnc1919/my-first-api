from flask import Flask, jsonify
import random

app = Flask(__name__)

# This is your data "database"
facts = [
    {"id": 1, "fact": "The first computer bug was an actual moth found in a relay."},
    {"id": 2, "fact": "Python was named after the comedy group Monty Python."},
    {"id": 3, "fact": "The first web page is still online at info.cern.ch."}
]

@app.route('/')
def home():
    return "Welcome to my Free Fact API! Go to /random to see a fact."

@app.route('/random')
def get_fact():
    return jsonify(random.choice(facts))

if __name__ == '__main__':
    app.run()
