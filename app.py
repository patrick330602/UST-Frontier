from flask import Flask, request, jsonify
import json
import os

import quicksort


app  = Flask(__name__)


@app.route('/sort', methods=['POST'])
def sort():
	if request.method == 'POST':
		content = request.body
		data  = json.loads(content)
		new = quicksort.quickSort(data)
		return jsonify(new)
	else:
		pass