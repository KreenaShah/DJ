graph={
  '5':['3','7'],
  '3': ['2', '4'],
  '7': ['8'],
  '2': [],
  '4': ['8'],
  '8': [],
}

visited=[]
queue=[]
closed_list=[]

def dfs(visited, graph,node,goal):
  visited.append(node)
  path={}
  path[node]=node
  root=[]
  queue.append(node)
  print(f'Open List: {queue}\nClosed List: {closed_list}\n')

  while queue:
    m=queue.pop()
    closed_list.append(m)
    print(f'Open List: {queue}\nClosed List: {closed_list}\n')

    if(m==goal):
      while path[m]!=m:
        root.append(m)
        m=path[m]
      root.append(m)
      root.reverse()
      print(f"\nPath: {root}")  
      return

    for neighbour in graph[m]:
      if neighbour not in visited:
        visited.append(neighbour)
        queue.append(neighbour)
        path[neighbour]=m
    print(f'Open List: {queue}\nClosed List: {closed_list}\n')

  print("Path does not found")

dfs(visited,graph,'5','2')