from collections import deque
import heapq

n, k = map(int, input().split())
arr = [[]]

temp = []
q = deque()
heap = []
def dfs(count):
    while q:
        virus, x, y = q.popleft()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 < nx <= n and 0 < ny <= n:
                if arr[nx][ny] == 0:
                    arr[nx][ny] = virus
                    q.append((virus, nx, ny))
        count -= 1

        if count == 0:
            return


dx = [-1, 1, 0, 0] # 상하좌우
dy = [0, 0, -1, 1]

for i in range(1, n+1):
    arr.append(list(map(int, input().split())))
    arr[i].insert(0, 0)
    for j in range(n+1):
        if arr[i][j]:
            temp.append((arr[i][j], i, j))# 바이러스 종류, 행, 열
            #heapq.heappush(heap, (arr[i][j], (i, j)))
            #q.append((arr[i][j], i, j))# 바이러스 종류, 행, 열


count = 1
while True: # 너무 무식하게 넣었는데 더 깔끔한 방법은 없을까?
    for i in range(len(temp)):
        if temp[i][0] == count:
            q.append((temp[i][0], temp[i][1], temp[i][2]))
    count += 1
    if count > k:
        break



s, x, y = map(int, input().split())

for i in range(s):
    dfs(len(q))

print(arr[x][y])





