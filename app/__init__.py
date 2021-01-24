from flask import *
from .utils.decorators import errorhandle

app = Flask(__name__)


@app.route("/")
def index():
	return {
		"status":200,
		"message":"api is active!"
	}

@app.route("/error")
@errorhandle
def error():
	raise Exception("death")
	return "something bad"
