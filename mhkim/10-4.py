"""
@file 10-4.py
@brief 커리큘럼
@desc 위상 알고리즘

위상 알고리즘을 수행, 더 오랜 시간 걸리는 경우의 시간 값을 저장하는 방식으로 결과 테이블 갱신하여 출력
"""
from collections import deque
import copy


v = int(input())
indegree = [0] * (v + 1)
graph = [[] for i in range(v + 1)]
time = [0] * (v + 1)

for i in range(1, v + 1):
    data = list(map(int, input().split()))
    time[i] = data[0]
    for x in data[1:-1]:
        indegree[i] += 1
        graph[x].append(i)


def topology_sort():
    result = copy.deepcopy(time)
    q = deque()

    for i in range(1, v + 1):
        if indegree[i] == 0:
            q.append(i)

    while q:
        now = q.popleft()
        for i in graph[now]:
            result[i] = max(result[i], result[now] + time[i])
            indegree[i] -= 1

            if indegree[i] == 0:
                q.append(i)

    for i in range(1, v + 1):
        print(result[i])


topology_sort()