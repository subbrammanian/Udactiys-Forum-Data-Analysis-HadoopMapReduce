#!/usr/bin/python

import sys
top10 = [None]*10
len10 = [None]*10

prevkey=None
total = 0

for line in sys.stdin:
	data_mapped = line.strip().split("\t")
	if len(data_mapped) != 2:
		continue
	
	key,value = data_mapped

	if prevkey and prevkey!=key:
		for i in range(10):
			if not top10[i]:
				top10[i]=prevkey
				len10[i]=total
				break
			if total>len10[i]:
				for j in range(9,i,-1):
					top10[j] = top10[j-1]
					len10[j] = len10[j-1]
				top10[i] = prevkey
				len10[i] = total
				break
		total = 0	
	total += int(value)
	prevkey = key
	
for i in range(10):
			if not top10[i]:
				top10[i]=prevkey
				len10[i]=total
				break
			if total>len10[i]:
				for j in range(9,i,-1):
					top10[j] = top10[j-1]
					len10[j] = len10[j-1]
				top10[i] = prevkey
				len10[i] = total
				break

for i in range(10):
	print top10[i],"\t",len10[i]