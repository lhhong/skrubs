def evaluate(inputVal):
    inputVal.sort()
    if len(inputVal) < 2:
        return {"answer": 0}
    minDiff = abs(inputVal[0] - inputVal[1])
    oldV = inputVal[1]
    for i in inputVal[2:]:
        if abs(oldV - i) < minDiff:
            minDiff = abs(oldV - i)

    return {"answer": minDiff}

tests = [
    [1,22,53,13,1254,651,12]
]
