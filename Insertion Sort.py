#Insertion sort. Runs in O(n^2) time
def insertion_sort(a):
	l = len(a)
	for i in xrange(1,l):
		j = i
		while j > 0 and a[j-1] > a[j]:
			a[j], a[j-1] = a[j-1], a[j]
			j = j-1

	return a

testArray = [1,3,5,2,4,6]
print insertion_sort(testArray)
