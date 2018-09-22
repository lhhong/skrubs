from itertools import compress

def evaluate(data):

    targetSum = data["input"]
    print(targetSum)

    def generatePrimesFrom2(n):
        """ Returns a list of primes < n for n > 2 """
        sieve = bytearray([True]) * (n//2+1)
        for i in range(1,int(n**0.5)//2+1):
            if sieve[i]:
                sieve[2*i*(i+1)::2*i+1] = bytearray((n//2-2*i*(i+1))//(2*i+1)+1)
        return [2, *compress(range(3,n,2), sieve[1:])]

    answer = []
    primes = generatePrimesFrom2(targetSum)

    if targetSum%2 == 1:
        answer.append(3)
        targetSum = targetSum -3
        primes = primes[2:]

    for prime in primes:
        test = targetSum - prime
        if test in primes:
            answer.append(test)
            answer.append(prime)
            return answer

tests = [
{ "input": 791076 }
]
