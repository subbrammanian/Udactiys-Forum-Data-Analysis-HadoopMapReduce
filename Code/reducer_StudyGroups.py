#!/usr/bin/python

import sys
prevkey=None
current_list=[] 	

for line in sys.stdin:
	data_mapped = line.strip().split("\t")
	if len(data_mapped) != 2:
		continue
	
	key,value = data_mapped

	if prevkey and prevkey!=key:
		print prevkey,"\t",current_list
		current_list = []
		
	current_list.append(int(value))
	prevkey = key
	
print prevkey,"\t",current_list