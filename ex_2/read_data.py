### CURSO DE ANÁLISE DE DADOS COM PYTHON - CERTI
### RAFAEL CALIXTO
### LEITURA DE ARQUIVOS LOCAIS

############################
input("Primeiramente vamos ver como importar dados de um arquivo em formato CSV")
############################

from csv import reader

file = reader(open("data.csv"), delimiter="\t")

[print(row) for row in file]

############################
input("Agora vamos ver como importar dados de um arquivo em formato JSON")
############################

from json import load
from pprint import pprint

file = load(open("data.json"))
pprint(file)
