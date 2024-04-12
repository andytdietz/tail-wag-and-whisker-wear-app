from flask import Flask, request
import db

app = Flask(__name__)


@app.route("/outfits.json")
def index():
    return db.outfits_all()





@app.route("/outfits/<id>.json")
def show(id):
    return db.outfits_find_by_id(id)