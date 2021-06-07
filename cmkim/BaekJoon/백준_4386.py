import sys, math, heapq
n = int(input())

arr = []
connected = []
sum = 0
cost = 1e9

def dist(x1, y1, x2, y2):
    return math.sqrt((x1 - x2)**2 + (y1 - y2)**2)

for i in range(n):
    x, y = map(float, input().split())
    arr.append((x, y))

q = []
connected.append(0)
for i in range(1, n):
    heapq.heappush(q, (dist(arr[0][0], arr[0][1], arr[i][0], arr[i][1]), i))

# print(connected)
# print(q)

while n != len(connected):
    value, node = heapq.heappop(q)
    while node in connected:
        value, node = heapq.heappop(q)

    sum += value
    connected.append(node)

    for i in range(n):
        if i not in connected:
            heapq.heappush(q, (dist(arr[node][0], arr[node][1], arr[i][0], arr[i][1]), i))

print("%.2f"%(sum))












