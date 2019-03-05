from csv import reader

file = reader(open("data.csv"), delimiter="\t")

[print(row) for row in file]
