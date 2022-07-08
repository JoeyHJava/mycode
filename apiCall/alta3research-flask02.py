import requests
import json
from pprint import pprint

url = "http://127.0.0.1:2224"

age = 22
new_std = {
    "name": "two",
    "age": age 
}


resp = requests.post(url + "/login")
# pprint("/login on 2: ",resp)

post_rp = requests.post(url + "/body")
pprint(post_rp)