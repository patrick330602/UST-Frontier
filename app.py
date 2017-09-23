from flask import Flask, request, jsonify, Response
import json
import os

import countsort
import newsort
import knapsack
import area
import stringcom 
import schedule
import train


app  = Flask(__name__)

@app.route('/sort', methods=['POST'])
def sort():
	content = request.get_json()
	data = newsort.sort(content)
	return Response(response=json.dumps(data), status=200, mimetype="application/json")

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
	out = knapsack.KnapsackFrac(values, weight, maxWeight)
	return jsonify({"heist": int(out)})

@app.route('/calculateemptyarea', methods=['POST'])
def calculateemptyarea():
	data = request.get_json()
	result = 0.0
	if 'circle' in data:
		result = area.circle(data["container"]["coordinate"]["X"],data["container"]["coordinate"]["Y"],data["container"]["width"],data["container"]["height"],data["circle"]["center"]["X"],data["circle"]["center"]["Y"],data["circle"]["radius"])
	elif 'square' in data:
		result = area.square(data["container"]["coordinate"]["X"],data["container"]["coordinate"]["Y"],data["container"]["width"],data["container"]["height"],data["square"]["coordinate"]["X"],data["square"]["coordinate"]["Y"],data["square"]["width"])
	elif 'rectangle' in data:
		result = area.rectangle(data["container"]["coordinate"]["X"],data["container"]["coordinate"]["Y"],data["container"]["width"],data["container"]["height"],data["rectangle"]["coordinate"]["X"],data["rectangle"]["coordinate"]["Y"],data["rectangle"]["width"],data["rectangle"]["height"])
	return jsonify(result)

@app.route('/stringcompression/<endr>', methods=['POST'])
def stringcompression(endr):
	data = request.get_json()
	inp = data["data"]
	result = 0
	if endr == "RLE":
		result = stringcom.RLE(inp)
	elif endr == "LZW":
		result = stringcom.LZW(inp)
	elif endr == "WDE":
		result = stringcom.WDE(inp)
	return jsonify(result)

@app.route('/releaseSchedule', methods=['POST'])
def releaseSchedule():
	data = request.get_json()
	out = schedule.schedule(data)
	return jsonify(out)

@app.route('/trainPlanner', methods=['POST'])
def trainPlanner():
	data = request.get_json()
	line, totalNumOfPassengers, reachingVia = train.train(data)
	return jsonify({"line": line,"totalNumOfPassengers": totalNumOfPassengers,"reachingVia": reachingVia})
