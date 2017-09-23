from flask import Flask
import requests
import json
import os

import quicksort


app  = Flask(__name__)


@app.route('/')
def index():
	return "Thank you for visiting this site for demo!"

@app.route('/sort', methods=['POST'])
def sort():
	content = quicksort.quickSort([1,2,3,4])
	return content