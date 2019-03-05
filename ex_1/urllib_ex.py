from urllib3 import PoolManager as pm
from json import loads
from pprint import pprint

r = pm().request("GET", "https://blockchain.info/unconfirmed-transactions?format=json")
data = r.data.decode("utf-8")
json_data = loads(data)

pprint(json_data)
