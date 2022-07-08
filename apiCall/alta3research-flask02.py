import requests
import json
from pprint import pprint

url = "http://127.0.0.1:2224"

age = 22
new_std = {
    "name": "David",
    "pw": age 
}

resp = requests.post(url + "/login")

post_rp = requests.get(url + "/body")

resp= requests.get(url + "/readable").json()

pprint(resp)
