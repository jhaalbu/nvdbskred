import requests
import json

longitude =6.144475002129221
latitude = 60.256895003124455
params = dict(lon = longitude, lat = latitude )
u = 'https://www.vegvesen.no/nvdb/api/vegreferanse/koordinat.json'
resp = requests.get(url=u, params=params)
data = json.loads(resp.text)

print(data['visningsNavn'])

print(data.keys())