import re
from collections import defaultdict

def evaluate(inputValue):
    # data = inputValue['data']
    # graph = {}
    # distances = {}
    # allNodes = set()
    # for d in data:
    #     node = re.split('->|,', d)
    #     allNodes.add(node[0])
    #     allNodes.add(node[1])
    #     if node[0] not in graph:
    #         graph[node[0]] = {}
    #     if node[1] not in graph:
    #         graph[node[1]] = {}
    #     graph[node[0]][node[1]] = node[2]
    # sender = inputValue['sender']
    # recipient = inputValue['recipient']
    #
    # dist = set()
    # prev = set()
    class Graph:
      def __init__(self):
        self.nodes = set()
        self.edges = defaultdict(list)
        self.weights = {}

      def add_node(self, value):
        self.nodes.add(value)

      def add_edge(self, from_node, to_node, weight):

        self.edges[from_node].append(to_node)
        # self.edges[to_node].append(from_node)
        self.weights[(from_node, to_node)] = weight

    def dijsktra(graph, initial, end):
    # shortest paths is a dict of nodes
    # whose value is a tuple of (previous node, weight)
        shortest_paths = {initial: (None, 0)}
        current_node = initial
        visited = set()

        while current_node != end:
            visited.add(current_node)
            destinations = graph.edges[current_node]
            weight_to_current_node = shortest_paths[current_node][1]

            for next_node in destinations:
                weight = graph.weights[(current_node, next_node)] + weight_to_current_node
                if next_node not in shortest_paths:
                    shortest_paths[next_node] = (current_node, weight)
                else:
                    current_shortest_weight = shortest_paths[next_node][1]
                    if current_shortest_weight > weight:
                        shortest_paths[next_node] = (current_node, weight)

            next_destinations = {node: shortest_paths[node] for node in shortest_paths if node not in visited}
            if not next_destinations:
                return "Route Not Possible"
            # next node is the destination with the lowest weight
            current_node = min(next_destinations, key=lambda k: next_destinations[k][1])

        # Work back through destinations in shortest path
        path = []
        while current_node is not None:
            path.append(current_node)
            next_node = shortest_paths[current_node][0]
            current_node = next_node
        # Reverse path
        path = path[::-1]
        return path

    graph = Graph()
    data = inputValue['data']
    for d in data:
        node = re.split('->|,', d)
        graph.add_node(node[0])
        graph.add_node(node[1])
        graph.add_edge(node[0], node[1], int(node[2]))

    print(graph.edges)
    sender = inputValue['sender']
    recipient = inputValue['recipient']

    visited = {sender: 0}
    path = {}

    nodes = set(graph.nodes)

    # while nodes:
    #     min_node = None
    #     for node in nodes:
    #       if node in visited:
    #         if min_node is None:
    #           min_node = node
    #         elif visited[node] < visited[min_node]:
    #           min_node = node
    #
    #     if min_node is None:
    #       break
    #
    #     nodes.remove(min_node)
    #     current_weight = visited[min_node]
    #
    #     for edge in graph.edges[min_node]:
    #       weight = current_weight + graph.distances[(min_node, edge)]
    #       if edge not in visited or weight < visited[edge]:
    #         visited[edge] = weight
    #         path[edge] = min_node
    # print(path)
    return dijsktra(graph, sender, recipient)


    # visited = {sender: 0}
    # path = {}
    #
    # while allNodes:
    #     min_node = None
    #     for node in allNodes:
    #         if node in visited:
    #             if min_node is None:
    #                 min_node = node
    #             elif visited[node] < visited[min_node]:
    #                 min_node = node
    #     if min_node is None:
    #         break
    #     nodes.remove(min_node)
    #     current_weight = visited[min_node]
    #
    #     for edge in graph[min_node]:
    #         weight = 0



    # S = []
    # return

tests = [{
    "data" : [ "A->B,1000" , "A->C,4500" , "B->D,2000" , "B->C,1000", "E->F,4000" ],
    "sender" : "A",
    "recipient" : "C"
}]
