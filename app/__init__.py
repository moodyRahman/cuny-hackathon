from flask import *
from .utils.decorators import errorhandle
import requests as r

app = Flask(__name__)


@app.route("/")
def index():
	return {
		"status":200,
		"message":"api is active!"
	}

@app.route("/compliment")
def compliment():
	return r.get("https://complimentr.com/api").json()

@app.route("/error")
@errorhandle
def error():
	raise Exception("death")
	return "something bad"
