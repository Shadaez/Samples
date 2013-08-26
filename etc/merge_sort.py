import math

def merge_sort(list):
	length = len(list)
	if length <= 1:
		return list
	left = merge_sort(list[length/2:])
	right = merge_sort(list[:length/2])
	sort = []
	while len(sort) < length:
		if len(left) != 0 and len(right) != 0:
			if left[0] < right[0]:
				sort.append(left.pop(0))
			else:
				sort.append(right.pop(0))
		else:
			sort.extend(left + right)
	else:
		return sort

assert merge_sort([1,3,2,5,4,6,8,7,9,0,.5]) == [0,.5,1,2,3,4,5,6,7,8,9]
assert merge_sort([1]) == [1]
assert merge_sort([1,1,1,1,1]) == [1,1,1,1,1]
assert merge_sort([1.1,1.2,1.3,1.4,.9,.8,.7]) == [.7,.8,.9,1.1,1.2,1.3,1.4]
assert merge_sort([70.920,-38.797,14.354,99.323,90.374,7.581]) == [-38.797,7.581,14.354,70.920,90.374,99.323]
longmerge = [1,5,1,61,5,1,77,72,7,83,38,4,8,9854,85,548,548,54,5,6,25,23,42,34,24,234,2,3425,2,627,4,8,83,3,4,34,34,3,4,3]
sortedmerge = [1,5,1,61,5,1,77,72,7,83,38,4,8,9854,85,548,548,54,5,6,25,23,42,34,24,234,2,3425,2,627,4,8,83,3,4,34,34,3,4,3]
sortedmerge.sort()
assert merge_sort(longmerge) == sortedmerge
print 'success'
