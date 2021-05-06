from collections import deque

def BFS(graph, v, visited):

    queue = deque([v])
    visited[v] = 1

    while(queue):
        v = queue.popleft() #시작 기준이 되는 값을 잡고 시작한다.
        print(v, end=' ')   # end= ' '  -> 다음 출력값 사이의 간격 조정(줄바꿈도 생략가능)

        for i in graph[v]:  #기준값 주변에 있는 방문하지 않은 값들을 전부 탐색한다.
            if not visited[i]:
                queue.append(i)
                visited[i] = 1




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


BFS(graph, 1, visited) #사용할 graph, 시작노드, 방문여부