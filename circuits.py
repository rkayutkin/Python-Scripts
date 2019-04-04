import pip
import csv

with open('circuits.csv', newline='') as csvfile:
	reader = csv.DictReader(csvfile)
	for row in reader:
		print(row['Circuit ID'], row['ifName'])