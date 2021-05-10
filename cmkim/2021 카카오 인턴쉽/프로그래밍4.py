from collections import deque

#INF = 1000000000


def solution(n, start, end, roads, traps):
    visited = [[0] * (n + 1) for _ in range(n+1)]
    answer = 1000000
    while q:
        #print('roads = ', roads)
        start, roads, traps, cost = q.popleft()

        if start == end:
            answer = min(answer, cost)
            continue

        for a, b, c in roads: # 출발, 도착, 비용
            if start == a : # 이동할 다음노드가 있으면 이동
                if b not in traps: #다음노드가 정상적으로 이동할 노드면
                    if not visited[a][b]:
                        visited[a][b] = 1
                        q.append((b, roads, traps, cost+c))
                    continue
                else: # 다음노드가 함정노드면
                    if not visited[a][b]:
                        visited[a][b] = 1

                        for i in range(len(roads)):
                            if roads[i][0] == b or roads[i][1] == b:
                                temp = roads[i][0]
                                roads[i][0] = roads[i][1]
                                roads[i][1] = temp
                        q.append((b, roads, traps, cost+c))



    print(answer)
    return answer
q = deque()

# n = 3
# start = 1
# end = 3
# roads = [[1, 2, 2], [3, 2, 3]]
# traps = [2]

n = 4
start = 1
end = 4
roads = [[1, 2, 1], [3, 2, 1], [2, 4, 1]]
traps = [2, 3]

q.append((start, roads, traps, 0)) #마지막은 cost
solution(n, start, end, roads, traps)