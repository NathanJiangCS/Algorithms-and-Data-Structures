#2 Examples of Merge Sort in Python, one using Heapq and one Without
#This is using merge from heapq
from heapq import merge
 
 #m is the array that is to be sorted
def merge_sort(m):
    if len(m) <= 1:
        return m
 
    middle = len(m) // 2
    left = m[:middle]
    right = m[middle:]
 
    left = merge_sort(left)
    right = merge_sort(right)
    return list(merge(left, right))

#Without merge from heapq, we have:
def mergeSort(x):
#Divinding the array into 2 subarrays
	mid = len(x) / 2
	leftArray = x[:mid]
	rightArray = x[mid:]
	#Checking that the array is at least 2 elements in length
	if len(x) > 1:
		#Recursively performing mergeSort on each half
	    mergeSort(leftArray)
	    mergeSort(rightArray)
	    i, j = 0, 0 #Indices of a and b
	    a = leftArray; b = rightArray
	    for k in range(len(a) + len(b) + 1):
	        if a[i] <= b[j]:
	            x[k] = a[i]
	            i += 1
	            #If we are at the end of subarray a, copy the rest
				#of subarray b to our result list
	            if i == len(a) and j != len(b):
	                while j != len(b):
	                    k +=1
	                    x[k] = b[j]
	                    j += 1
	                break
	        elif a[i] > b[j]:
	            x[k] = b[j]
	            j += 1
	            #If we are at the end of subarray b, copy the rest
	        	#of subarray a to our result list
	            if j == len(b) and i != len(a):
	                while i != len(a):
	                    k+= 1
	                    x[k] = a[i]
	                    i += 1                    
	                break
	return x

testArray = [1,4,3,6,2,5,8,4]
print mergeSort(testArray)
print merge_sort(testArray)
