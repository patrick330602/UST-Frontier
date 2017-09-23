from flask import Flask, request, jsonify
import simplejson as sj
import os

import quicksort
import greedy


app  = Flask(__name__)

@app.route('/sort', methods=['POST'])
def sort():
	content = request.get_json()
	data  = quicksort.quickSort(content)
	return jsonify(data)

@app.route('/heist', methods=['POST'])
def heist():
	data = request.get_json()
	maxWeight = data["maxWeight"]
	vault = data["vault"]
	values=[]
	weight=[]
	for value in vault:
		values.append(value["value"])
		weight.append(value["weight"])
	out = greedy.KnapsackFrac(values, weight, maxWeight)
	out_final = []
	out_final["heist"]= out
	return jsonify(out_final)

app.run(debug=True)