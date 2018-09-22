import math
from itertools import count, islice

def evaluate(inputValue):
    def isPrime(n):
        return n > 1 and all(n%i for i in islice(count(2), int(math.sqrt(n)-1)))

    #inputValue = inputValue["input"]
    if isPrime(inputValue):
        return [inputValue]

    primes = []
    for possiblePrime in range(2, inputValue):
        # Assume number is prime until shown it is not.
        is_Prime = True
        for num in range(2, possiblePrime):
            if possiblePrime % num == 0:
                is_Prime = False
        if is_Prime:
            primes.append(possiblePrime)

    #primes.append(1)
    primes = sorted(primes, reverse = True)
    if not primes:
        print "list is empty"
    tempPrimes = primes[:]
    if not tempPrimes:
        print "list is empty"
    currVal = inputValue
    currList = []
    n = 0

    while currVal != 0:
        currVal = inputValue
        print "tempPrimes = ",  tempPrimes
        if not tempPrimes:
            return None
        for i in tempPrimes:
            if currVal - i == 0:
                currList.append(i)
                return currList
            elif currVal - i > 0:
                currVal = currVal - i
                currList.append(i)
        tempPrimes.pop(0)

    # def sum_of_primes(value):
    #     primes = prime_sieve(value)
    #     lo = 0
    #     hi = len(primes) - 1
    #     while lo <= hi:
    #         prime_sum = primes[lo] + primes[hi]
    #         if prime_sum < value:
    #             lo += 1
    #         else:
    #             if prime_sum == value:
    #                 yield primes[lo], primes[hi]
    #             hi -= 1
    # return

tests = [
    6,
    21,
    100,
    96,
    21,
    15

]
