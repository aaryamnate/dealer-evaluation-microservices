import os
from flask import Flask, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # lets the frontend call this API from the browser

PRODUCTS = [
    {"id": 1, "name": "Toyota Camry"},
    {"id": 2, "name": "Honda Civic"},
    {"id": 3, "name": "Ford Mustang"},
    {"id": 4, "name": "Tesla Model 3"},
    {"id": 5, "name": "Hyundai Elantra"},
]

@app.route("/")
def home():
    return jsonify({"service": "product-details", "status": "running"})

@app.route("/products")
def get_products():
    return jsonify(PRODUCTS)

@app.route("/products/<int:product_id>")
def get_product(product_id):
    for p in PRODUCTS:
        if p["id"] == product_id:
            return jsonify(p)
    return jsonify({"error": "Product not found"}), 404

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 8080)))
