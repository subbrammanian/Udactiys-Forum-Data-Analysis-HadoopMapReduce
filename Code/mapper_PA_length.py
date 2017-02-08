#!/usr/bin/python

# Format of each line is:
# date\ttime\tstore name\titem description\tcost\tmethod of payment


import sys
import re
import csv

reader = csv.reader(sys.stdin, delimiter='\t')
writer = csv.writer(sys.stdout, delimiter='\t', quotechar='"', quoting=csv.QUOTE_ALL)

for line in reader:
	
	if len(line)==19:
		postid,body,nodetype,parentid = line[0].strip(),line[4].strip(),line[5].strip(),line[6].strip()
		
		if nodetype=="question":
			print postid,"\t",["q",len(body)]
		elif nodetype=="answer":
			print parentid,"\t",["a",len(body)]
		else:
			pass
		
		

