from queue import PriorityQueue

def dijkstra(graph, start):
    print(len(graph))
    visited = {}
    D = {}
    D[start] = 0

    pq = PriorityQueue()
    pq.put((graph[start], start))

    while not pq.empty():
        (dist, current) = pq.get()
        visited[current] = True
        for neighbour, distance in graph[current].items():
            if neighbour not in visited:
                old_cost = D.get(neighbour, float("inf"))
                new_cost = D[current] + distance
                if new_cost < old_cost:
                    pq.put((new_cost, neighbour))
                    D[neighbour] = new_cost
    return D

def create_graph(arr):
    graph = {} 
    
    # create all vertices
    for row, _ in enumerate(arr):
        for col, _ in enumerate(arr[row]):
            graph[(row, col)] = {}

    # add edges between vertices
    for node, _ in graph.items():
        row, col = node

        # up neighbour
        if (row-1,col) in graph:
            graph[(row,col)][(row-1, col)] = arr[row-1][col]
        # down neighbour
        if (row+1,col) in graph:
            graph[(row,col)][(row+1, col)] = arr[row+1][col]
        # left neighbour
        if (row,col-1) in graph:
            graph[(row,col)][(row, col-1)] = arr[row][col-1]
        # right neighbour
        if (row,col+1) in graph:
            graph[(row, col)][(row, col+1)] = arr[row][col+1]

    return graph


def create_tiled_graph(arr):
    tiled_arr = [[0 for _ in range(len(arr)*5)] for _ in range(len(arr)*5)]

    i = 0
    for r in range(5):
        for c in range(5):
            for row, _ in enumerate(arr):
                for col, _ in enumerate(arr[row]):
                    value = arr[row][col] + (c+r) if arr[row][col] + (c+r) < 10 else abs(9 - arr[row][col] - (c+r))
                    tiled_arr[row+(r*(len(arr)))][col+(c*(len(arr[row])))] = value

    graph = {}
    
    # create all vertices
    for row, _ in enumerate(tiled_arr):
        for col, _ in enumerate(tiled_arr[row]):
            graph[(row, col)] = {}

    # add edges between vertices
    for node, _ in graph.items():
        row, col = node

        # up neighbour
        if (row-1,col) in graph:
            graph[(row,col)][(row-1, col)] = tiled_arr[row-1][col]
        # down neighbour
        if (row+1,col) in graph:
            graph[(row,col)][(row+1, col)] = tiled_arr[row+1][col]
        # left neighbour
        if (row,col-1) in graph:
            graph[(row,col)][(row, col-1)] = tiled_arr[row][col-1]
        # right neighbour
        if (row,col+1) in graph:
            graph[(row, col)][(row, col+1)] = tiled_arr[row][col+1]

    return graph

with open("input.txt") as file:
    arr = []
    
    for line in file.readlines():
        arr.append([int(c) for c in line.strip()])

    #print(graph)
    p1_graph=create_graph(arr)
    p2_graph=create_tiled_graph(arr)
    
    D = dijkstra(p1_graph, (0,0))
    print("part_one", D[(len(arr)-1, len(arr)-1)])

    D = dijkstra(p2_graph, (0,0))
    print("part_two", D[(len(arr)*5-1, len(arr)*5-1)])