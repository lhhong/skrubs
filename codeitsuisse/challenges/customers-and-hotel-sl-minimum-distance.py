def evaluate(inputVal):

    inputVal.sort()
    if len(inputVal) < 2:
        return {"answer": 0}
    minDiff = inputVal[1] - inputVal[0]
    oldV = inputVal[1]
    for i in inputVal[2:]:
        if i - oldV < minDiff:
            minDiff = i - oldV
        oldV = i

    return {"answer": minDiff}

tests = [
    [1,22,53,13,1254,651,12]
]
