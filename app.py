from flask import Flask, request, jsonify
import json
import os

import quicksort
import greedy


app  = Flask(__name__)


@app.route('/sort', methods=['POST'])
def sort():
	content = request.get_json()
	data  = quicksort.quickSort(content)
	return jsonify(data)

@app.route('/heist', methods=['POST'], endpoint="heist")
def heist():
	content = request.get_json()
	data  = json.loads(content)
	maxWeight = data["maxWeight"]
	vault = data["vault"]
	values=[]
	weight=[]
	for value in vault:
		values.append(value["value"])
		weight.append(value["weight"])
	out = greedy.KnapsackFrac(values, weight, maxWeight)
	return jsonify(out)