def evaluate(inputVal):
    print(inputVal)
    A = inputVal["calories_for_each_type_for_raphael"]
    B = inputVal["calories_for_each_type_for_leonardo"]
    diff = inputVal["maximum_difference_for_calories"]
    modding = 100000123

    minmin = min(min(A), min(B))

    A = [a - minmin for a in A]
    B = [b - minmin for b in B]

    aSum = sum(A)
    bSum = sum(B)

    A_table = {}
    B_table = {}

    def srA(h, v):
        A_table[h] = v
        return v

    def srB(h, v):
        B_table[h] = v
        return v

    def findNoCombi(i, d, array, sr, table):
        h = (i, d)
        if h in table:
            return table[h]

        if i < -1:
            return sr(h, 0)

        if d == 0:
            return sr(h, 1)

        if d < 0:
            return sr(h, 0)

        combi = sum([
            findNoCombi(i-1, d, array, sr, table),
            findNoCombi(i-1, d-array[i], array, sr, table)
        ])
        combi %= modding

        return sr(h, combi)

    result = 0
    for i in range(aSum+1):
        aRes = findNoCombi(len(A)-1, i, A, srA, A_table)

        for j in range(i-diff, i+diff + 1):

            abRes = aRes * findNoCombi(len(B)-1, j, B, srB, B_table)
            result += abRes
            result %= modding

    return {"result": result}

#    dp_table = {}
#
#    def sr(h, v):
#        dp_table[h] = v
#        return v
#
#    def findNoCombi(aI, bI, d):
#        h = (aI, bI, d)
#        if h in dp_table:
#            return dp_table[h]
#
#        if aI < -1 or bI < -1:
#            return sr(h, 0)
#
#        if aI < 0 and bI < 0:
#            if d == 0:
#                return sr(h, 1)
#            else:
#                return sr(h, 0)
#
#        if aI < 0 or bI < 0:
#            if d == 0:
#                return sr(h, 1)
#
#        combi = sum([
#            findNoCombi(aI-1, bI, d),
#            findNoCombi(aI-1, bI, d-A[aI]),
#            findNoCombi(aI, bI-1, d),
#            findNoCombi(aI, bI-1, d+A[bI]),
#        ])
#        combi %= modding
#
#        return sr(h, combi)
#
#    result = 0
#    for i in range(-diff, diff):
#        result += findNoCombi(len(A)-2, len(A)-2, i)
#        result %= modding
#
#    return {"result": result}

tests = [
    {
        "number_of_types_of_food" : 2,
        "calories_for_each_type_for_raphael" : [4,5],
        "calories_for_each_type_for_leonardo" :  [3,6],
        "maximum_difference_for_calories": 3
    }
]

