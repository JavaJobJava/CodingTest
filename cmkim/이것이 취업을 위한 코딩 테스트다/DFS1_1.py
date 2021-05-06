def DFS(graph, v, visited):

    visited[v] = 1
    print(v,end = ' ') # end= ' '  -> 다음 출력값 사이의 간격 조정(줄바꿈도 생략가능)

    for i in graph[v]:
        if not visited[i]:
            DFS(graph, i, visited)

visited = [0]*9
graph = [
  [],
  [2, 3, 8],
  [1, 7],
  [1, 4, 5],
  [3, 5],
  [3, 4],
  [7],
  [2, 6, 8],
  [1, 7]
]


DFS(graph, 1, visited) #사용할 graph, 시작노드, 방문여부