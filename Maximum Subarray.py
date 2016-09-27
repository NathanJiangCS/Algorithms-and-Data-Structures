#Solution to maximum subarray problem
#given an array of length n
#find the contiguous subarray which has the largest sum

#Two different solutions are given below

#If the result can be a zero length subarray:
def maxSubarray(A):
    maxEndingHere = maxSoFar = 0
    for x in A:
        maxEndingHere = max(0, maxEndingHere + 1)
        maxSoFar = max(maxEndingHere, maxSoFar)

    return maxSoFar


#If the result cannot be a zero-length subarray

def maxSubarray(A):
    maxEndingHere = maxSoFar = A[0]
    for x in A[1:]:
        maxEndingHere = max(x, maxEndingHere + x)
        maxSoFar = max(maxEndingHere, maxSoFar)

    return maxSoFar
