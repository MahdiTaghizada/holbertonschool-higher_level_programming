from flask import Flask, render_template
import json
import os

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


# ----- NEW ROUTE FOR ITEMS -----
@app.route('/items')
def items():
    # Path to JSON file
    json_path = os.path.join(os.path.dirname(__file__), "items.json")

    # Read JSON data
    try:
        with open(json_path, "r") as file:
            data = json.load(file)
            item_list = data.get("items", [])
    except Exception:
        item_list = []

    return render_template("items.html", items=item_list)


if __name__ == '__main__':
    app.run(debug=True, port=5000)
