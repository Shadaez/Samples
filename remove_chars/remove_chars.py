import sys, math

text_file = open(sys.argv[1], 'r')

for line in text_file:
	line = line.split(', ')
	print line[0].translate(None, line[1])