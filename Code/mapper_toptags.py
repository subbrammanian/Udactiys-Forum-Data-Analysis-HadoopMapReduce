#!/usr/bin/python

# Format of each line is:
# date\ttime\tstore name\titem description\tcost\tmethod of payment


import sys
import csv

reader = csv.reader(sys.stdin, delimiter='\t', quotechar='"', quoting=csv.QUOTE_ALL)
writer = csv.writer(sys.stdout, delimiter='\t', quotechar='"', quoting=csv.QUOTE_ALL)

for line in reader:
	if len(line)==19:
		tagnames = line[2].strip()
		tagnames = tagnames.split(" ")
		for val in tagnames:
			val = val.strip()
			print val,"\t",1