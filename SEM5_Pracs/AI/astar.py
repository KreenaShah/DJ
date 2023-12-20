def astar(graph, hn, start, goal):
    openList = [{ 'node': start, 'g': 0, 'h': hn[start], 'f': 0 + hn[start], 'parent': None }]
    closedList = []

    while openList:
        openList.sort(key=lambda node: node['f'])
        currentNode = openList.pop(0)

        if currentNode['node'] == goal:
            path = []
            while currentNode:
                path.insert(0, currentNode['node'])
                currentNode = currentNode['parent']
            return path

        closedList.append(currentNode)

        for neighbor, cost in enumerate(graph[currentNode['node']]):
            if cost > 0 and neighbor not in [node['node'] for node in closedList]:
                g = currentNode['g'] + cost
                h = hn[neighbor]
                f = g + h
                neighborNode = { 'node': neighbor, 'g': g, 'h': h, 'f': f, 'parent': currentNode }

                if neighbor not in [node['node'] for node in openList] or f < openList[0]['f']:
                    openList.append(neighborNode)
    return None

gn = [
    [0, 4, 3, 0, 0, 0, 0],
    [0, 0, 0, 0, 12, 5, 0],
    [0, 0, 0, 7, 10, 0, 0],
    [0, 0, 0, 0, 2, 0, 0],
    [0, 0, 0, 0, 0, 0, 5],
    [0, 0, 0, 0, 0, 0, 16],
    [0, 0, 0, 0, 0, 0, 0]
]

hn = [14, 12, 11, 6, 4, 11, 0]

start_node = 0
goal_node = 6

path = astar(gn, hn, start_node, goal_node)

if path:
    print("A* Path :", path)
else:
    print("No path found.")