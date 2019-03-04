### CURSO DE ANÁLISE DE DADOS COM PYTHON - CERTI
### RAFAEL CALIXTO
### AQUISIÇÃO DE DADOS DA WEB

from pprint import pprint
import requests

api = "https://blockchain.info/latestblock"
### retorna um json com as informações do último bloco
### minerado na blockchain do bitcoin

r = requests.get(api)

print("status da requisição >>", r.status_code)
print("tipo de encode >>", r.encoding)
print("a string retornada possui ", len(r.text), "caracteres")

block = r.json()
del block["txIndexes"]

pprint(block)
