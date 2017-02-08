#!/usr/bin/python

import sys

prevkey=None
myCounter = {}

for line in sys.stdin:
	data_mapped = line.strip().split("\t")
	if len(data_mapped) != 2:
		continue

	key,hour = data_mapped

	if prevkey and prevkey!=key:
		#Find maximum from the dictionary, print it, reset the dictionary
		maxV = 0
		for v in myCounter.values():
			if v>maxV: maxV = v
		for k,v in myCounter.items():
			#print "K value",k
			if v == maxV:
				print prevkey.strip(),'\t',k
		myCounter={}

	myCounter[hour] = myCounter.get(hour,0)+1
	prevkey=key

maxV = 0
for v in myCounter.values():
	if v>maxV: maxV = v
for k,v in myCounter.items():
	if v == maxV:
		print prevkey.strip(),'\t',k