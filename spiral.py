"""
input text file =
3;3;1 2 3 4 5 6 7 8 9
feel free to do your own tests!
"""


def spiralPrint(width, height, array): #recursive! :D
	if width <= 0 or height <= 0:
		return []
	elif width <= 1:
		return array[-1]
	elif height <= 1:
		spiral = []
		for i in range(width):
			spiral.append(array[i][0])
		return spiral
	else:
		spiral = []
		spiral.extend(array.pop(0)) #top
		temp = []
		for i in range(width-1):
			temp.append(array[-(i+1)].pop(0))
			spiral.append(array[i].pop(-1))
		spiral.extend((array.pop(-1)[::-1]))
		spiral.extend(temp)
		spiral.extend(spiralPrint(width-2, height-2, array))
		return spiral

text_file = open("spiraltext.txt", 'r')

for line in text_file:
	w, h, a = line.strip().split(';')
	w, h = int(w), int(h)
	a = [[str(x) for x in a.split(' ')][i*h:h+i*h] for i in range(w)]
	print ' '.join(spiralPrint(w, h, a))
"""output should be =
1 2 3 6 9 8 7 4 5
"""
