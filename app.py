from flask import Flask, request, jsonify
import json
import os

import quicksort


app  = Flask(__name__)


@app.route('/sort', methods=['POST'])
def sort():
	content = request.get_json()
	data  = quicksort.quickSort(content)
	return jsonify(data)