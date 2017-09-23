import requests
url = 'http://cis2017-coordinator.herokuapp.com/api/evaluate'
#url = 'http://127.0.0.1:5000/heist'
response = requests.post(url, json={"team": "UST Frontier","challenge": "Calculate Empty Area"})
print(response.headers)
print(response.content)
