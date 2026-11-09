import csv
with open("ruba.csv","r",newline="",encoding="UTf-8")as ruba:
  reader=csv.reader(file)
  for row in reader:
    print(row)