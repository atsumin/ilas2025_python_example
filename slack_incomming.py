import requests
import pprint

server = 'https://hooks.slack.com/services/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'
data = {'text': 'python request test: last_name'}

r = requests.post(server, json=data)

print('request data')
pprint.pprint(r.request.__dict__)

