def evaluate(inputVal):

    print(inputVal)
    ranges = [(x["pos"] - x["distance"], x["pos"] + x["distance"]) for x in inputVal]
    ranges.sort(key=lambda x: x[0])
    camps = []

    for i in ranges:
        if len(camps) == 0:
            camps.append([i[0], i[1]])
        if i[0] <= camps[-1][1]:
            camps[-1][0] = i[0]
            if i[1] <= camps[-1][1]:
                camps[-1][1] = i[1]
        else:
            camps.append([i[0], i[1]])

    return {"answer": len(camps)}


tests = [
    [
        {
            "pos":4,
            "distance":3
        },
        {
            "pos":7,
            "distance":1
        },
        {
            "pos":5,
            "distance":1
        },
        {
            "pos":1,
            "distance":1
        }
    ]
]
