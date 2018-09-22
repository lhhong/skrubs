def evaluate(inputVal):
    puzzle = inputVal["puzzle"]

    if len(puzzle) == 3:
        moves = {0: {1, 3}, 1:{0, 2, 4}, 2:{1, 5}, 3:{0, 4, 6}, 4:{1, 3, 5, 7}, 5:{2, 4, 8}, 6:{3, 7}, 7:{4, 6, 8}, 8:{5,7}}
        goal = (1,2,3,4,5,6,7,8,0)
    elif len(puzzle) == 4:
        moves = {0: {1, 4}, 1:{0, 2, 5}, 2:{1, 3, 6}, 3:{2, 7}, 4:{0, 5, 8}, 5:{1,4,6,9}, 6:{2,5,7,10}, 7:{3,6,11}, 8:{4,9,12},
                 9:{5,8,10,13}, 10:{6,9,11,14}, 11:{7,10,15}, 12:{8,13}, 13:{9,12,14}, 14:{10,13,15}, 15:{11,14}}
        goal = (1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,0)
    else:
        return {"result":[]}

    used, cnt = set(), 0
    ans = []

    s = tuple([c for row in puzzle for c in row])
    q = [([], s, s.index(0))]
    while q:
        new = []
        for a, s, i in q:
            used.add(s)
            if s == goal:
                return {"result": a}
            arr = list(s)
            for move in moves[i]:
                new_arr = arr[:]
                new_ans = a[:]
                new_ans.append(new_arr[move])
                new_arr[i], new_arr[move] = new_arr[move], new_arr[i]
                new_s = tuple(new_arr)
                if new_s not in used:
                    new.append((new_ans, new_s, move))
        cnt += 1
        q = new
    return {"result":[]}

tests = [
    {
        "puzzle":[
            [1,2,3],
            [4,8,5],
            [7,6,0]
        ]
    },
    {"puzzle": [[2, 3, 6], [7, 4, 0], [8, 5, 1]]}
]
