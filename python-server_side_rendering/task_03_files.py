import csv
import json
import os

from flask import Flask, render_template, request

app = Flask(__name__)

def read_json_data(file_path):
    with open(file_path, "r", encoding="utf-8") as f:
        return json.load(f)

def read_csv_data(file_path):
    with open(file_path, "r", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        return list(reader)

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

@app.route("/product")
def product():
    source = request.args.get("source")
    product_id = request.args.get("id")

    data = []
    error = None
    status_code = 200

    try:
        if source == "json":
            print("Reading data from JSON file")
            data = read_json_data("products.json")
        elif source == "csv":
            print("Reading data from CSV file")
            data = read_csv_data("products.csv")
        else:
            error = "Invalid source. Use ?source=json or ?source=csv"
            print(error)
            status_code = 400

        if product_id and status_code == 200:
            print(f"Filtering product with ID: {product_id}")
            data = [item for item in data if item.get("id") == product_id]
            if not data:
                error = f"No product found with ID: {product_id}"
                status_code = 404

    except Exception as e:
        error = f"An error occurred: {str(e)}"
        print(error)
        status_code = 500

    return render_template("product_display.html", products=data, error=error), status_code
if __name__ == '__main__':
   app.run(debug=True, port=5000)