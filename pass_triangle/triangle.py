"""Pass Triangle

Challenge Description:

By starting at the top of the triangle and moving to adjacent numbers on the row below, the maximum total from top to bottom is 27.

   5
  9 6
 4 6 8
0 7 1 5
5 + 9 + 6 + 7 = 27
Input sample:

Your program should accept as its first argument a path to a filename. Input example is the following

5
9 6
4 6 8
0 7 1 5
You make also check full input file which will be used for your code evaluation.
Output sample:

The correct output is the maximum sum for the triangle. So for the given example the correct answer would be

27"""
import sys

text_file = open(sys.argv[1], 'r')

triangle = []
for line in text_file:
	#make 2d list of ints
	triangle.append([int(num) for num in line.split(' ') if num != '\n'])
else:
	while len(triangle) != 1:
		bottom = triangle.pop()
		for index in range(len(triangle[-1])):
			if bottom[index] > bottom[index+1]:
				triangle[-1][index] += bottom[index]
			else:
				triangle[-1][index] += bottom[index+1]
	else:
		print triangle[-1][-1]