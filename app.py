from flask import Flask, request, jsonify
import json
import os

import quicksort


app  = Flask(__name__)


@app.route('/sort', methods=['POST'])
def sort():
	if request.method == 'POST':
		content = request.get_json()
		data  = quicksort.quickSort(content)
				return jsonify(new)
	else:
		pass