#solved.ac
#골드5
#다익스트라
#지름길
#1446

#다익스트라

import sys, heapq

input = sys.stdin.readline
INF = int(1e9)
distance = [INF]*10001
maps = [[] for _ in range(10001)]
startNodes = set()
N,D = map(int,input().split())

#그래프 정보 입력 
for i in range(N):
    a,b,c = map(int,input().split())
    startNodes.add(a)
    maps[a].append((b,c))
#distance 초기화 
for i in range(10001):
    distance[i]=i


#다익스트라 
def dijkstra(start,D):
    q = []
    heapq.heappush(q,(0,start))
    while q:
        cost,v = heapq.heappop(q)
        # #처리된 노드면 패스 
        if distance[v] < cost:
            continue
        #v에서 갈 수 있는 지름길 체크 
        for start in startNodes:
            #start가 이미 지난 지점이면 패스 
            if start<v:
                continue
            for info in maps[start]:
                dest,c = info
                #목적지보다 길면 패스(역주행 안됨)
                if dest>D:
                    continue
                #v에서 start까지 거리 계산해서 비용에 더해줌 
                c += cost+start-v
                # 지름길 비용과 지름길로 안갔을 때를 비교 
                if c < distance[v]+(dest-v):
                    distance[dest]= min(distance[dest],c) #start->dest 가 여러개일 수 있음
                    distance[D] = min(c+D-dest,distance[D]) # 0~v까지 비용 + 지름길 도착지 ~ D 까지 비용 과 비교 
                    heapq.heappush(q,(c,dest))

dijkstra(0,D)

print(distance[D])



