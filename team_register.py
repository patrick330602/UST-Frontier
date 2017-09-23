import requests
url = 'http://cis2017-coordinator.herokuapp.com/api/teams'
data = '''
{
    "name": "UST Frontier",
    "url": "http://ust-frontier.herokuapp.com",
    "members": ["Liu Chengzhong","Wang GUanzhi", "Wu Jinming"]
}'''
response = requests.post(url, data=data)
print(response)