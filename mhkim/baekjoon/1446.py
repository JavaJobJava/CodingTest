"""
@file 1446.py
@brief 지름길
@desc 다잌스트라

DP로도 풀 수 있을 것 같음
"""
import sys
import heapq
input = sys.stdin.readline
INF = int(1e9)

n, d = map(int, input().split())
graph = [[] for _ in range(d+1)]
distance = [i for i in range(d+1)]

for _ in range(n):
    start, dest, shortcut = map(int, input().split())
    if dest <= d:
        graph[start].append((dest, shortcut))

for i in range(d+1):
    if i > 0:
        distance[i] = min(distance[i], distance[i-1]+1)
    for j in graph[i]:
        if distance[i]+j[1] < distance[j[0]]:
            distance[j[0]] = distance[i]+j[1]

print(distance[d])
