import math
from itertools import count, islice
import sys
import re
import numpy
from itertools import compress
sys.setrecursionlimit(2000)

def evaluate(data):
    #inputValue = inputValue["input"]
    targetSum = data["input"]
    print(targetSum)

    # def isPrime(n):
    #     return n > 1 and all(n%i for i in islice(count(2), int(math.sqrt(n)-1)))
    #print ("inputValue = ", inputValue)

    def generate_primes(n):
        primes = []
        for possiblePrime in range(2, targetSum):
            # Assume number is prime until shown it is not.
            is_Prime = True
            for num in range(2, possiblePrime):
                if possiblePrime % num == 0:
                    is_Prime = False
            if is_Prime:
                primes.append(possiblePrime)
        return primes

    def isprime(n):
        return re.compile(r'^1?$|^(11+)\1+$').match('1' * n) is None

    def generatePrimesFrom2(n):
        """ Returns a list of primes < n for n > 2 """
        sieve = bytearray([True]) * (n//2+1)
        for i in range(1,int(n**0.5)//2+1):
            if sieve[i]:
                sieve[2*i*(i+1)::2*i+1] = bytearray((n//2-2*i*(i+1))//(2*i+1)+1)
        return [2, *compress(range(3,n,2), sieve[1:])]


    #primes.append(1)
    answer = []
    primes = generatePrimesFrom2(targetSum)

    if targetSum%2 == 1:
        answer.append(3)
        targetSum = targetSum -3
        primes = primes[2:]
    #print(primes)
    for prime in primes:
        test = targetSum - prime
        if test in primes:
            answer.append(test)
            answer.append(primes)
            return answer

    # dp_table = {}
    # if isPrime(targetSum):
    #     return [targetSum]
    #
    #
    # # primes = sorted(primes, reverse = True)
    # # tempPrimes = primes[:]
    # # discarded = []
    # # included = []
    # # currVal = inputValue
    # # n = 0
    # # i = 0
    #
    # def sumPrimes(index, target):
    #     #print(index, primes[index], target)
    #
    #     if (index, target) in dp_table:
    #         return dp_table[(index, target)]
    #
    #     if target == 0:
    #         dp_table[(index, target)] = []
    #         return dp_table[(index, target)]
    #
    #     if index < 0 or target < 0:
    #         dp_table[(index, target)] = False
    #         return dp_table[(index, target)]
    #
    #     include = sumPrimes(index - 1, target - primes[index])
    #     #print("include", include)
    #     if include!=False:
    #         #print(index, primes[index], target)
    #         include.append(primes[index])
    #         dp_table[(index, target)] = include
    #         #print(dp_table[(index, target)])
    #         return dp_table[(index, target)]
    #     else:
    #         exclude = sumPrimes(index - 1, target)
    #         #print("exclude", exclude)
    #         if exclude!=False:
    #             #print(index, primes[index], target)
    #             dp_table[(index, target)] = dp_table[(index - 1, target)]
    #             #print(index, target, dp_table[(index, target)])
    #             return dp_table[(index, target)]
    #
    #     dp_table[(index, target)] = False
    #     return dp_table[(index, target)]
    #
    # return(sumPrimes(len(primes)-1, targetSum))

    # def sumOfPrimes (n, listOfPrimes, included):
    #     if n == 0:
    #         return True
    #     if n < 0 or len(listOfPrimes) == 0:
    #         return False
    #     if n - listOfPrimes[-1] >= 0:
    #         included.append(listOfPrimes[-1])
    #     return sumOfPrimes(n - listOfPrimes[-1], listOfPrimes[:-1], included) or sumOfPrimes(n, listOfPrimes[:-1], included)
    #
    #     # currVal = n - listOfPrimes[0]
    #     # if currVal == 0:
    #     #     goodPrimes.append(listOfPrimes[0])
    #     #     return goodPrimes
    #     # elif n > 0:
    #     #     print ("n > 0")
    #     #     currVal = n - listOfPrimes[0]
    #     #     goodPrimes.append(listOfPrimes[0])
    #     #     print(goodPrimes)
    #     #     return sum_of_primes(currVal, goodPrimes)
    #
    #
    # sumOfPrimes(inputValue, primes, included)
    #
    # return included




    # def sumOfPrimes (n, listOfPrimes, discarded, included):
    #     if n == 0:
    #         return True
    #     if n < 0 or len(listOfPrimes) == 0:
    #         return False
    #     if sumOfPrimes(inputValue, listOfPrimes[:-1], discarded, included):
    #         discarded.append(listOfPrimes[-1])
    #         print("discarded: ", discarded)
    #     if sumOfPrimes(inputValue - listOfPrimes[-1], listOfPrimes[:-1], discarded, included):
    #         included.append(listOfPrimes[-1])
    #         print("included: ", included)
    #     return sumOfPrimes(inputValue, listOfPrimes[:-1], discarded, included) or sumOfPrimes(inputValue - listOfPrimes[-1], listOfPrimes[:-1], discarded, included)
    #
    # if sumOfPrimes(inputValue, primes, discarded, included):
    #     print ("help")
    #     return included
    # else:
    #     print ("that's wrong")
    #     return None



    # while currVal != 0:
    #     currVal = inputValue
    #     if not tempPrimes:
    #         return None
    #     for i in tempPrimes:
    #         if currVal - i == 0:
    #             currList.append(i)
    #             print ("currList = ",  currList)
    #             return currList
    #         elif currVal - i > 0:
    #             currVal = currVal - i
    #             currList.append(i)
    #     tempPrimes.pop(0)
    #     currList = []



    # primes = generate_primes(inputValue)
    # primes = sorted(primes, reverse = True)
    # tempPrimes = primes[:]
    # currVal = inputValue
    # currList = []
    # n = 0
    # i = 0
    # while currVal != 0:
    #     currVal = inputValue
    #     #print ("tempPrimes = ",  tempPrimes)
    #     if not tempPrimes:
    #         return None
    #     for i in tempPrimes:
    #         if currVal - i == 0:
    #             currList.append(i)
    #             print ("currList = ",  currList)
    #             return currList
    #         elif currVal - i > 0:
    #             currVal = currVal - i
    #             currList.append(i)
    #     tempPrimes.pop(0)
    #     currList = []


tests = [
{ "input": 219099 }
]
