import requests

received = ["Sorting","Jewellery Heist","Calculate Empty Area"]
url = 'http://cis2017-coordinator.herokuapp.com/api/evaluate'
for challenge in received:
    print()
    print(challenge)
    print("---------------")
    response = requests.post(url, json={"team": "UST Frontier","challenge": challenge})
    print(response.headers)
    print(response.content)
