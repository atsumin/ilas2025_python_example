import os
from dotenv import load_dotenv
import requests
import pprint

load_dotenv(".env")

server = os.environ.get("WEBHOOK_URL")
data = {'text': 'python request test: last_name'}

r = requests.post(server, json=data)

print('request data')
pprint.pprint(r.request.__dict__)

