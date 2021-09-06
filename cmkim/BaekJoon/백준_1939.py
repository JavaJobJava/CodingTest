# 처음엔 플로이드워셜 알고리즘을 사용하는 줄 알았는데
# 플로이드 워셜은 최솟값 구할때만 해당하는듯
# 이 문제는 이때동안 풀었던 유형이랑 좀 다른게
# 노드를 탐색해 나가며 최대 중량을 찾아 나가는게 아니라
# 최대 중량을 설정하고 이게 되는지 안되는지 판단해야됌
# 원래가 바텀업방식이라면 이건 탑다운 방식?  이 개념이 맞는지는 잘 모르겠다.
import sys
from _collections import deque
n, m = map(int, input().split())

def bfs(mid):

    q = deque()
    q.append(start_point)
    visited[start_point] = 1

    while q:
        start = q.popleft()
        if start == end_point:
            return True
        for n_node, n_cost in arr[start]:
            if visited[n_node] == 0 and mid <= n_cost:
                q.append(n_node)
                visited[n_node] = 1
    return False


arr = [[] for _ in range(n+1)]

for i in range(m):
    a, b, c = map(int, input().split())
    arr[a].append((b, c))
    arr[b].append((a, c))

start_point, end_point = map(int, input().split())


left, right = 1, 1e9
result = 0

while left <= right:
    visited = [0 for _ in range(n + 1)]
    mid = (left + right) // 2
    if bfs(mid): #중량이 통과했을때
        left = mid + 1
        result = mid
    else: #중량 통과 못했을때
        right = mid - 1

print(int(result))