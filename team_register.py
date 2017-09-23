import requests
import sys

num = sys.argv[1] 
received = ["Sorting","Jewellery Heist","Calculate Empty Area","String Compression", "Release Schedule"]
url = 'http://cis2017-coordinator.herokuapp.com/api/evaluate'
challenge = received[int(num)]
print()
print(challenge)
print("---------------")
response = requests.post(url, json={"team": "UST Frontier","challenge": challenge})
print(response.headers)
print(response.content)
