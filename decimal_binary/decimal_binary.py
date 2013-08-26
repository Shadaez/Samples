'''Decimal To Binary

Challenge Description:

Given a decimal (base 10) number, print out its binary representation.

Input sample:

File containing positive whole decimal numbers, one per line. e.g. 

2
10
67
Output sample:

Print the decimal representation, one per line.
e.g.

10
1010
1000011'''
import sys

text_file = open(sys.argv[1], 'r')

for line in text_file:
	print str(bin(int(line)))[2:]