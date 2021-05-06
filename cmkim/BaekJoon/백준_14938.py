# 각 지역에서 시작했을때 다른 지역까지의 거리를 모두 구할수 있어야한다 dijkstra를 통해서
# 그 이후 r보다 작은 값들에 있는 지역의 아이템 갯수를 모두 구해서 더하기


# 위의 과정들을 모든 시작점에 대해 반복해줘서 가장 큰 값 찾아서 출력하기
import sys, heapq


def dijkstra(start):
    sum = 0
    q = []
    distance = [INF] * (n + 1)
    distance[start] = 0

    heapq.heappush(q, [0, start]) #q에다 start 에서 자기 자신으로 가는 초기값 넣기

    while q:
        cur_distance, cur = heapq.heappop(q) # q에서 현재지점 current 까지의 distance 정보 가져오기

        for i in range(n+1):
            if 0 < d[cur][i] < INF:
                if d[cur][i] + cur_distance < distance[i]:
                    distance[i] = d[cur][i] + cur_distance
                    heapq.heappush(q, [distance[i], i])

    for i in range(1, n+1):
        if distance[i] <= m:
            sum += area_item[i]

    return sum

n, m, r = map(int, input().split())
INF = 1000000000
#area = [0]*(n+1)
d = [[INF] * (n+1) for _ in range(n+1)]
for i in range(n):
    d[i+1][i+1] = 0
result = 0  #최종적으로 출력할 정답

# 지역 마다의 자원의 갯수 입력받기
area_item = list(map(int, input().split()))
area_item.insert(0, 0)
#print(area_item)

# 지역별 이동거리를 인접 행렬로 입력 받기
for i in range(r):
    start, end, distance = map(int, input().split())
   #d[i+1][i+1] = 0
    d[start][end] = distance
    d[end][start] = distance

#print(d)

for i in range(n):
    if dijkstra(i+1) > result:
        result = dijkstra(i+1)

print(result)







