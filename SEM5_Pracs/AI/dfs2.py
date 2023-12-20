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

def dfs(start, goal):
    stack.append(start)
    visited[start] = True

    while stack:
        print("Open list:", stack)
        current = stack.pop()
        print("Visited Node:", current)

        if current == goal:
            print(f"Goal node {goal} found!")
            return

        for i in range(num_nodes - 1, -1, -1):
            if graph[current][i] == 1 and not visited[i]:
                stack.append(i)
                visited[i] = True

    print(f"Goal node {goal} not found!")

if __name__ == "__main__":
    start = int(input("Enter the start node: "))
    goal = int(input("Enter the goal node: "))

    if start < 0 or start >= num_nodes or goal < 0 or goal >= num_nodes:
        print("Invalid start or goal node.")
    else:
        dfs(start, goal)