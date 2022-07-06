import requests
import datetime
import reverse_geocode
from pprint import pprint
url= "http://api.open-notify.org/iss-now.json"
resp= requests.get(url)
astros= resp.json()

# tup =(float(astros['iss_position']['longitude']), float(astros['iss_position']['latitude']))
# print("tuple ", tup)
# loc = reverse_geocode.search(tup)
print(f"""CURRENT LOCATION OF THE ISS:
Timestamp: { datetime.datetime.fromtimestamp(astros['timestamp'])}
Long: {astros['iss_position']['longitude']}
Lat: {astros['iss_position']['latitude']}
""")
# City/Country: {loc}
