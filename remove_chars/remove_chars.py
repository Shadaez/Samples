"""Remove Characters  Share on LinkedIn

Challenge Description:

Write a program to remove specific characters from a string.

Input sample:

The first argument will be a text file containing an input string followed by a comma and then the characters that need to be scrubbed. e.g. 

how are you, abc
hello world, def
Output sample:

Print to stdout, the scrubbed strings, one per line. Trim out any leading/trailing whitespaces if they occur. 
e.g.

how re you
hllo worl
"""
import sys

text_file = open(sys.argv[1], 'r')

for line in text_file:
	line = line.split(', ')
	print line[0].translate(None, line[1])