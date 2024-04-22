from flask import Flask, request, jsonify
import json
import os

app = Flask(__name__)
ITEMS_FILE = 'items.json'

def load_items():
    if os.path.exists(ITEMS_FILE):
        with open(ITEMS_FILE, 'r') as file:
            data = json.load(file)
            return data['items']
    else:
        return []

def save_items(items):
    with open(ITEMS_FILE, 'w') as file:
        json.dump({"items": items}, file)

def next_item_id():
    items = load_items()
    return max(item['id'] for item in items) + 1 if items else 1

@app.route('/items', methods=['POST'])
def add_item():
    name = request.form.get('name')
    category = request.form.get('category')
    if not name or not category:
        return jsonify({"error": "Missing name or category"}), 400
    
    items = load_items()
    item_id = next_item_id()
    items.append({"id": item_id, "name": name, "category": category})
    save_items(items)
    return jsonify({"message": f"item received: {name}", "id": item_id}), 201

@app.route('/items', methods=['GET'])
def get_items():
    items = load_items()
    return jsonify({"items": items}), 200

@app.route('/items/<int:item_id>', methods=['GET'])
def get_item(item_id):
    items = load_items()
    item = next((item for item in items if item['id'] == item_id), None)
    if item:
        return jsonify(item), 200
    else:
        return jsonify({"error": "Item not found"}), 404

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=9000)
