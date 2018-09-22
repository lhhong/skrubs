def evaluate(inputVal):
    data = inputVal['data']
    graph = {}
    reverseGraph = {}
    allNodes = set()
    for d in data:
        node = d.split('->')
        allNodes.add(node[0])
        allNodes.add(node[1])
        if node[0] not in graph:
            graph[node[0]] = set()
        if node[1] not in graph:
            graph[node[1]] = set()
        graph[node[0]].add(node[1])

    S = []

    def dfs(graph, start, visited, fn):
        visited.add(start)
        for n in graph[start] - visited:
            dfs(graph, n, visited, fn)
        fn(start)
        return visited


    all_visited = set()
    for n in allNodes:
        if n not in all_visited:
            all_visited.union(dfs(graph, n, all_visited, lambda start: S.append(start)))

    ans = []
    all_visited = set()
    while len(S) > 0:
        n = S.pop()
        ans.append(n)
        def removal(s):
            if s in S:
                S.remove(s)
        all_visited.union(dfs(graph, n, all_visited, lambda s: removal(s)))

    return {"result": ans}

tests = [
    {
        "data" : [ "A->B" , "A->C" , "B->D" , "E->F" ]
    }
]

