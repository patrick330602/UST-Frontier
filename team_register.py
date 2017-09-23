import requests
url = 'http://cis2017-coordinator.herokuapp.com/api/evaluate'
response = requests.post(url, json={"team": "UST Frontier","challenge": "Sorting"})
print(response.headers)
print(response.content)