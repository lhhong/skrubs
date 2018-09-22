def evaluate(inputVal):
    data = inputVal['data']
    graph = {}
    reverseGraph = {}
    allNodes = set()
    nodes = allNodes.copy()
    for d in data:
        node = d.split('->')
        allNodes.add(node[0])
        allNodes.add(node[1])
        if node[0] not in graph:
            graph[node[0]] = set()
        if node[1] not in graph:
            graph[node[1]] = set()
        graph[node[0]].add(node[1])

        if node[0] not in reverseGraph:
            reverseGraph[node[0]] = set()
        if node[1] not in reverseGraph:
            reverseGraph[node[1]] = set()
        reverseGraph[node[1]].add(node[0])

    S = []

    def dfs(graph, start, visited, fn):
        visited.add(start)
        count = 1
        for n in graph[start] - visited:
            count += dfs(graph, n, visited, fn)[1]
        fn(start)
        return visited, count


    all_visited = set()
    while len(allNodes) > 0:

        def removalAN(s):
            if s in allNodes:
                allNodes.remove(s)
            S.append(s)

        n = allNodes.pop()
        all_visited.union(dfs(graph, n, all_visited, lambda start: removalAN(start))[0])


    scc = []
    SS = S[:]
    all_visited = set()
    while len(SS) > 0:

        def removal(s):
            if s in SS:
                SS.remove(s)
            scc[-1].append(s)

        n = SS.pop()
        scc.append([])
        all_visited.union(dfs(reverseGraph, n, all_visited, lambda s: removal(s))[0])

    S = [min(x) for x in scc]

    ans = []
    all_visited = set()
    all_count = {}
    while len(S) > 0:
        n = S.pop()
        ans.append(n)

        def removal(s):
            if s in S:
                S.remove(s)

        v, count = dfs(graph, n, all_visited, lambda s: removal(s))
        all_visited.union(v)
        all_count[n] = count

    maxC = 0
    maxN = None
    for k, v in all_count.items():
        if v >= maxC:
            if maxN == None or k < maxN:
                maxC = v
                maxN = k

    return {"result": maxN}

tests = [
    {
        "data" : [ "A->B" , "A->C" , "B->D" , "E->F" ]
    }
]


