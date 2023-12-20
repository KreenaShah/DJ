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
closed = []
queue = []

def enqueue(node):
    queue.append(node)

def dequeue():
    if queue:
        return queue.pop(0)
    else:
        return None

def bfs(start, goal):
    enqueue(start)
    visited[start] = True

    while queue:
        print("Open list:", queue, end="\t\t")
        current = dequeue()
        closed.append(current)
        print("Closed list:", closed, end="\t\t")

        if current == goal:
            print(f"\nGoal node {goal} found!")
            return
        else:
            print(f"{current} not goal", end="\n")

        for i in range(num_nodes):
            if graph[current][i] == 1 and not visited[i]:
                enqueue(i)
                visited[i] = True

    print(f"Goal node {goal} not found!")

if __name__ == "__main__":
    start = int(input("Enter the start node: "))
    goal = int(input("Enter the goal node: "))

    if start < 0 or start >= num_nodes or goal < 0 or goal >= num_nodes:
        print("Invalid start or goal node.")
    else:
        bfs(start, goal)