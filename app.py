from flask import Flask, render_template
import requests
import json
import os


app  = Flask(__name__)


@app.route('/')
def index():
	return "Thank you for visiting this site for demo!"


app.run(debug=True)