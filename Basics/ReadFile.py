import csv

with open('example.csv') as file:
    readfile = csv.reader(file, delimiter=',')
    for row in readfile:
        print(row)
        print(row[0])
        print(row[1])
        print(row[0], row[1])
