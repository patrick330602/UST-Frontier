import requests
#url = 'http://cis2017-coordinator.herokuapp.com/api/evaluate'
url = 'http://127.0.0.1:5000/heist'
response = requests.post(url, json={"maxWeight": 4,"vault": [{"weight": 1, "value": 200},{"weight": 3, "value": 240},{"weight": 5, "value": 150},{"weight": 2, "value": 140}]})
print(response.headers)
print(response.content)
