from flask import Flask, request
import db

app = Flask(__name__)


@app.route("/outfits.json")
def index():
    return db.outfits_all()

