def evaluate(data):
    inputValue = data.get("input")
    primes = [inputValue%i != 0 for i in range(2, int(inputValue**0.5)+1)]
    return primes


tests = [{ "input": 19 }]
