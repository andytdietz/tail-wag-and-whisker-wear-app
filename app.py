from flask import Flask, request
import db

app = Flask(__name__)

@app.route('/')
def hello():
    return 'Hello, World!'

@app.route("/outfits.json")
def index():
    return db.outfits_all()

@app.route("/outfits.json", methods=["POST"])
def create():
    name = request.form.get("name")
    animal_id = request.form.get("animal_id")
    price = request.form.get("price")
    image_url = request.form.get("image_url")
    return db.outfits_create(name, animal_id, price, image_url)