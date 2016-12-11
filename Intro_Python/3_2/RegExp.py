#!/usr/bin/python

import re
hand = open ('regex_sum_340373.txt')
numlist = list()
for line in hand:
	line = line.rstrip()
	stuff = re.findall('[0-9]+',line)
	if len(stuff) < 1 : continue
	#print stuff
	#num = float(stuff)
	num = [int(i) for i in stuff]
	numlist.extend(num)
		
		
count = len(numlist)
sum = sum(numlist)
#print numlist	
print'count:', count, "sum", sum	