#Sieve of Eratosthenes is a prime number sieve that finds all prime numbers
#up till a limit.


from math import ceil


def sieveOfEratosthenes(n):
    if n < 1: 
        return 0

    primeList = [True for i in xrange(n)]
    primeList[0] = primeList[1] = False
    
    for i in xrange(2, int(ceil(n**0.5))):
        if primeList[i] == True:
            for j in xrange(2*i, n, i):
                primeList[j] = False

    return primeList #Array from 0 to n-1 with values of True indicating prime
                     #and False indicating not prime


        
