#!/usr/bin/python

# Format of each line is:
# date\ttime\tstore name\titem description\tcost\tmethod of payment


import sys
import csv
import datetime

reader = csv.reader(sys.stdin, delimiter='\t', quotechar='"', quoting=csv.QUOTE_ALL)
writer = csv.writer(sys.stdout, delimiter='\t', quotechar='"', quoting=csv.QUOTE_ALL)

for line in reader:
	if len(line)==19:
		authid,addedat = line[3].strip(),line[8].strip()
		if authid=='author_id' or addedat=='':	continue
		addedat = addedat[0:-3]
		addedat = datetime.datetime.strptime(addedat,'%Y-%m-%d %H:%M:%S.%f')
		print authid,"\t",addedat.hour

