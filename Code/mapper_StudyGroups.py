#!/usr/bin/python

# Format of each line is:
# date\ttime\tstore name\titem description\tcost\tmethod of payment


import sys
import csv

reader = csv.reader(sys.stdin, delimiter='\t', quotechar='"', quoting=csv.QUOTE_ALL)
writer = csv.writer(sys.stdout, delimiter='\t', quotechar='"', quoting=csv.QUOTE_ALL)

for line in reader:
	if len(line)==19 and line[0].strip()!="id":
		postid,authid,nodetype,parentid = line[0].strip(),line[3].strip(),line[5].strip(),line[6].strip()
		
		if nodetype == "question":
			print postid,"\t",authid
		else:
			print parentid,"\t",authid