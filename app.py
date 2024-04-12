from flask import Flask, request
import db

app = Flask(__name__)

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

@app.route("/outfits/<id>.json", methods=["DELETE"])
def destroy(id):
    return db.outfits_destroy_by_id(id)






@app.route("/outfits/<id>.json", methods=["PATCH"])
def update(id):
    name = request.form.get("name")
    animal_id = request.form.get("animal_id")
    price = request.form.get("price")
    image_url = request.form.get("image_url")
    return db.outfits_update_by_id(id, name, animal_id, price, image_url)