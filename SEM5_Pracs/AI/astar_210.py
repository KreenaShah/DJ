import queue

class Node:
    def __init__(self,state,grid,heuristic,cost = 0,parent= None):
        self.state = state
        self.grid = grid
        self.cost = cost
        self.parent = parent
        self.heuristic = heuristic
        
    def __lt__(self, other):
        return (self.cost + self.heuristic) < (other.cost + other.heuristic)
    
def define_path(node):
    path = []
    while node:
        path.append(node.state)
        node = node.parent
    return path[::-1]

def get_neighbors(state,grid):
    x , y = state
    neighbors = [(x+1,y), (x,y+1), (x-1,y), (x,y-1), (x+1,y+1), (x-1,y-1), (x-1,y+1), (x+1,y-1)]
    valid_neighbors = [(nx,ny) for nx, ny in neighbors if 0<=nx<=grid_length and 0<=ny<=grid_width]
    print(f'for state , {state} valid neighbors are {valid_neighbors}')
    valid_neighbors = [(nx,ny) for nx,ny in valid_neighbors if grid[nx][ny] == 0]
    print(f'final valid neighbors are {valid_neighbors}')
    return [(neighbor, 1) for neighbor in valid_neighbors]

def heuristic(current_state, goal_state):
    x1,y1 = current_state
    x2,y2 = goal_state
    return abs(x1-x2)+abs(y1-y2)

def astar(initial_state,goal_state,grid,heuristic):
    visited = set()
    openlist = queue.PriorityQueue()
    start_node = Node(initial_state,grid,heuristic(initial_state,goal_state),0,None)
    openlist.put(start_node)
    
    while not openlist.empty():
        current_node = openlist.get()
        
        if current_node.state == goal_state:
            return define_path(current_node)
        visited.add(current_node.state)
        
        for neighbors,cost in get_neighbors(current_node.state,grid):
            if neighbors not in visited:
                neighbor_node = Node(neighbors,grid,heuristic(neighbors,goal_state),current_node.cost+cost,current_node)
                openlist.put(neighbor_node)
    return -1

grid_width = 4
grid_length = 4
grid = [
    [0, 0, 0, 1, 1],
    [1, 0, 1, 0, 1],
    [0, 1, 1, 1, 0],
    [0, 1, 0, 1, 0],
    [0, 0, 0, 0, 0]
]
# 1 - closed
# 0 - open

path = astar((0,0),(4,4),grid,heuristic)
if path == -1:
    print("no path exist")
else:
    print(path)