from flask import Flask, request, jsonify
import json
import os

import quicksort


app  = Flask(__name__)


@app.route('/')
def index():
	return "Thank you for visiting this site for demo!"

@app.route('/sort', methods=['POST'])
def sort():
	content = request.get_json()
	
	return content