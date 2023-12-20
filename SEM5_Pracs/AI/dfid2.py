graph = [
    [0, 1, 1, 1, 0, 0, 0],
    [1, 0, 1, 0, 1, 0, 0],
    [1, 1, 0, 0, 1, 0, 0],
    [1, 0, 0, 0, 0, 0, 1],
    [0, 1, 1, 0, 0, 1, 0],
    [0, 0, 0, 0, 1, 0, 1],
    [0, 0, 0, 1, 0, 1, 0],
]
num_nodes = 7

visited = [False] * num_nodes
stack = []
top = -1

def dfs(start, goal, depth):
    global top
    if start == goal:
        print(f"Goal node {goal} found")
        return True
    if depth <= 0:
        return False
    
    stack.append(start)
    top += 1
    visited[start] = True

    for i in range(num_nodes):
        if graph[start][i] == 1 and not visited[i]:
            if dfs(i, goal, depth - 1):
                return True

    visited[start] = False
    stack.pop()
    top -= 1

    return False

def dfid(start, goal):
    for d in range(100):
        if all(visited):
            return
        if dfs(start, goal, d):
            return
    print(f"Goal node {goal} not found!")

if __name__ == "__main__":
    start = int(input("Enter the start node: "))
    goal = int(input("Enter the goal node: "))

    if start < 0 or start >= num_nodes or goal < 0 or goal >= num_nodes:
        print("Invalid start or goal node.")
    else:
        dfid(start, goal)