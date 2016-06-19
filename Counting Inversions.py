# O(nlogn) implementation of counting inversions using extended merge sort
def merge_sort(a):
	if len(a) <= 1:
		return 0, a
	middle = len(a)/2
	left_inversions, l = merge_sort(a[:middle])
	right_inversions, r = merge_sort(a[middle:])
	merge_inversions, m = merge(l,r)
	inversions = left_inversions + right_inversions + merge_inversions
	return inversions, m

def merge(left, right):
	result = []
	i,j,count = 0,0,0
	while i < len(left) and j < len(right):
		if left[i] < right[j]:
			result.append(left[i])
			i += 1
		else:
			count += (len(left) - i)
			result.append(right[j])
			j += 1

	
	result += left[i:]
	result += right[j:]

	return count, result


testArray = [1,3,5,2,4,6]
inversions, sortedArray = merge_sort(testArray)
print inversions
print sortedArray
