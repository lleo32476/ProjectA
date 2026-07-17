from flask import Flask, jsonify, request
from flask_cors import CORS
from Functions import get_address
from StoreFinder import store_finder

app = Flask(__name__)

CORS(app)

@app.route("/get_address", methods=["POST"])
def get_address_function():
    data = request.get_json()
    street_address = data["street_address"]
    city = data["city"]
    state = data["state"]
    zip_code = data["zip_code"]

    return get_address(street_address, city, state, zip_code)

@app.route("/StoreFinder", methods=["POST"])
def store_finder_function():
    data = request.get_json()
    address = data["address"]
    lookup_item = data["lookup_item"]

    return store_finder(address, lookup_item)

if __name__ == "__main__":
    app.run(debug=True)