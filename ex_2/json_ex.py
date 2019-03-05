from json import load
from pprint import pprint

file = load(open("data.json"))
pprint(file)
