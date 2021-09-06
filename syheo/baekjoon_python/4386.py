#solved.ac
#골드4
#스패닝 트리
#별자리 만들기
#4386

import math
import heapq

def distance(a,b,c,d):
    return math.sqrt((a-c)**2+(b-d)**2)

n = int(input())
stars = [] 
connected = []
answer = 0 

for i in range(n):
    stars.append(tuple(map(float,input().split())))

connected.append(0)
q = [] 
for i in range(1,n):
    heapq.heappush(q,(distance(stars[0][0],stars[0][1],stars[i][0],stars[i][1]),i))

while len(connected)!=n:
    value, node = heapq.heappop(q)
    # 힙에 들어가있는 것은 connected에 들어있는 정점들과 연결 되어있는 정점임.
    # 만약 node 또한 힙에 연결되어 있는거라면 싸이클 발생 -> 두 정점이 connected에 있으면 싸이클 발생 
    while node in connected:
        value, node = heapq.heappop(q)
    answer+=value
    connected.append(node)
    #connected에서 만들 수 있는 간선들 추가 
    for i in range(n):
        if i not in connected:
            heapq.heappush(q,(distance(stars[node][0],stars[node][1],stars[i][0],stars[i][1]),i))
print("%.2f"%(answer))