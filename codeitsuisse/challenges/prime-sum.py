# import math
# from itertools import count, islice
#
# def evaluate(inputValue):
#     #inputValue = inputValue["input"]
#     def isPrime(n):
#         return n > 1 and all(n%i for i in islice(count(2), int(math.sqrt(n)-1)))
#     if isPrime(inputValue):
#         return [inputValue]
#
#     #print ("inputValue = ", inputValue)
#
#     def generate_primes(n):
#         primes = []
#         for possiblePrime in range(2, inputValue):
#             # Assume number is prime until shown it is not.
#             is_Prime = True
#             for num in range(2, possiblePrime):
#                 if possiblePrime % num == 0:
#                     is_Prime = False
#             if is_Prime:
#                 primes.append(possiblePrime)
#         return primes
#
#     #primes.append(1)
#
#     primes = generate_primes(inputValue)
#     tempPrimes = sorted(primes, reverse = True)
#     discarded = []
#     included = []
#     primeDict = {}
#     currList = []
#
#     currVal = inputValue
#     n = 0
#     i = 0
#
#     def sumOfPrimes (n, listOfPrimes):
#         if n == 0:
#             return True
#         if n < 0 or len(listOfPrimes) == 0:
#             return False
#         return sumOfPrimes(n, listOfPrimes[:-1]) or sumOfPrimes(n - listOfPrimes[-1], listOfPrimes[:-1])
#
#     # print(primes)
#     # return sumOfPrimes(inputValue, primes)
#
#     # def sum_of_primes (n, goodPrimes, i):
#     #     listOfPrimes = sorted(generate_primes(n), reverse = True)
#     #     for i in listOfPrimes:
#     #         if n - i > 0:
#     #             return sum_of_primes(n - listOfPrimes)
#     #         if n - i == 0:
#     #     return sum_of_primes(n - listOfPrimes)
#
#
#     while currVal != 0:
#         currVal = inputValue
#         #print ("tempPrimes = ",  tempPrimes)
#         if not tempPrimes:
#             return None
#         for i in tempPrimes:
#             if currVal - i < 0:
#                 continue
#             if currVal - i == 0:
#                 currList.append(i)
#                 print("primes: ", tempPrimes)
#                 print ("currList = ",  currList)
#                 return currList
#             elif currVal - i > 0:
#                 currVal = currVal - i
#                 currList.append(i)
#         tempPrimes.pop(0)
#         currList = []
#
#     print("primes: ", primes)
#     return currList
#
#
#
#
#
#
#
#
#
#
#     # print("included: ", included)
#     # # sumOfPrimes(inputValue, primes, included)
#     # if sumOfPrimes(inputValue, primes, included):
#     #     while currVal != 0:
#     #         currVal = inputValue
#     #         #print ("tempPrimes = ",  tempPrimes)
#     #         if not tempPrimes:
#     #             return None
#     #         for i in tempPrimes:
#     #             if currVal - i == 0:
#     #                 currList.append(i)
#     #                 print ("currList = ",  currList)
#     #                 return currList
#     #             elif currVal - i > 0:
#     #                 currVal = currVal - i
#     #                 currList.append(i)
#     #         tempPrimes.pop(0)
#     #         currList = []
#
#
#
#
#
#     # def sumOfPrimes (n, listOfPrimes, discarded, included):
#     #     if n == 0:
#     #         return True
#     #     if n < 0 or len(listOfPrimes) == 0:
#     #         return False
#     #     if sumOfPrimes(inputValue, listOfPrimes[:-1], discarded, included):
#     #         discarded.append(listOfPrimes[-1])
#     #         print("discarded: ", discarded)
#     #     if sumOfPrimes(inputValue - listOfPrimes[-1], listOfPrimes[:-1], discarded, included):
#     #         included.append(listOfPrimes[-1])
#     #         print("included: ", included)
#     #     return sumOfPrimes(inputValue, listOfPrimes[:-1], discarded, included) or sumOfPrimes(inputValue - listOfPrimes[-1], listOfPrimes[:-1], discarded, included)
#     #
#     # if sumOfPrimes(inputValue, primes, discarded, included):
#     #     print ("help")
#     #     return included
#     # else:
#     #     print ("that's wrong")
#     #     return None
#
#
#
#     # while currVal != 0:
#     #     currVal = inputValue
#     #     if not tempPrimes:
#     #         return None
#     #     for i in tempPrimes:
#     #         if currVal - i == 0:
#     #             currList.append(i)
#     #             print ("currList = ",  currList)
#     #             return currList
#     #         elif currVal - i > 0:
#     #             currVal = currVal - i
#     #             currList.append(i)
#     #     tempPrimes.pop(0)
#     #     currList = []
#
#
#
#     # primes = generate_primes(inputValue)
#     # primes = sorted(primes, reverse = True)
#     # tempPrimes = primes[:]
#     # currVal = inputValue
#     # currList = []
#     # n = 0
#     # i = 0
#     # while currVal != 0:
#     #     currVal = inputValue
#     #     #print ("tempPrimes = ",  tempPrimes)
#     #     if not tempPrimes:
#     #         return None
#     #     for i in tempPrimes:
#     #         if currVal - i == 0:
#     #             currList.append(i)
#     #             print ("currList = ",  currList)
#     #             return currList
#     #         elif currVal - i > 0:
#     #             currVal = currVal - i
#     #             currList.append(i)
#     #     tempPrimes.pop(0)
#     #     currList = []
#
#
# tests = [
#     100000
#
# ]
