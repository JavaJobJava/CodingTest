import heapq
import sys
input = sys.stdin.readline
n, k = map(int, input().split())

jewel = []
bags = []

for i in range(n):
    w, v = map(int, input().split())
    heapq.heappush(jewel, (w, v))

for i in range(k):
    heapq.heappush(bags, int(input()))

result = 0
selected = []
for _ in range(k):
    bags_weight = heapq.heappop(bags)

    while jewel and bags_weight >= jewel[0][0]:
        tmp = heapq.heappop(jewel)
        w, v = tmp[0], tmp[1]
        heapq.heappush(selected, -v)

    if selected:
        result -= heapq.heappop(selected)

print(result)
'''
4 4
1 100
2 200
13 300
10 500
14
3
12
1
'''