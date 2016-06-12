#Simple code for bubble sort. Runs in O(n^2) time
def bubble_sort(a):
	l = len(a)
	for i in xrange(1,l):
		for j in xrange(0,l-1):
			if a[j] > a[j+1]:
				a[j], a[j+1] = a[j+1], a[j]
	return a

testArray = [1,3,5,2,4,6]
sortedArray = bubble_sort(testArray)

print sortedArray
