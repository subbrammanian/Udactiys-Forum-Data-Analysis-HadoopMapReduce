#!/usr/bin/python

import sys

oldKey = None
outputstuff=[None]*13
prevkey=None
alenlist = []
qlen = 0

for line in sys.stdin:
	data_mapped = line.strip().split("\t")
	if len(data_mapped) != 2:
		continue
	
	key,content = data_mapped
	content = content[1:len(content)-1]
	content = content.replace("'","")
	content = content.strip().split(",")
	
	for i in range(len(content)):
		content[i] = content[i].strip()

	ntype = content[0]
	length = content[1]

	if prevkey and prevkey!=key:
		print qlen,"\t",sum(alenlist)/max(len(alenlist),1.0)
		qlen=0
		alenlist=[]

	if ntype == "q":
		qlen = length
	elif ntype == "a":
		alenlist.append(float(length))
	prevkey=key

print qlen,"\t",sum(alenlist)/max(len(alenlist),1)