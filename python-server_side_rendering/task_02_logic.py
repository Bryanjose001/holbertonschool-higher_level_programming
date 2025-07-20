import json
import os

from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
   return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/items')
def show_items():
    items = []

    # Read items from items.json
    json_path = os.path.join(os.path.dirname(__file__), 'items.json')
    if os.path.exists(json_path):
        with open(json_path, 'r') as file:
            data = json.load(file)
            items = data.get("items", [])

    return render_template('items.html', items=items)

if __name__ == '__main__':
   app.run(debug=True, port=5000)