#CH9 최단 경로
#예제 9-5
#전보

#N개 도시 
#C 도시 위급 상황
#메시지를 보낼 수 있는 총 도시 수, 총 걸리는 시간 출력 

import heapq

INF = int(1e9)
#도시 수 , 도로 수, 메시지 보내는 도시 
N,M,C = map(int,input().split())

#각 노드에 연결되어 있는 노드에 대한 정보를 담는 리스트 만들기
graph = [ [] for i in range(N+1)]

#최단 거리 테이블을 모두 무한으로 초기화
distance = [INF] * (N+1)

#모든 간선 정보를 입력받기
for _ in range(M):
    a,b,c = map(int, input().split())
    # a번 노드에서 b번 노드로 가는 비용이 c라는 의미
    graph[a].append((b,c))


def dijkstra(start):
    q = []
    #시작 노드에 대하여 초기화 ( 시작노드 데이터를 큐에 삽입)
    heapq.heappush(q,(0,start))
    distance[start] = 0
    while q: #큐가 비어있지 않다면
        # 가장 최단 거리가 짧은 노드에 대한 정보 꺼내기 
        dist, now = heapq.heappop(q)
        #현재 노드가 이미 처리된 적이 있는 노드라면 무시
        if distance[now] < dist:
            continue
        #현재 노드와 연결된 다른 입접한 노드들을 확인
        for i in graph[now]:
            cost = dist + i[1]
            #현재 노드를 거쳐서, 다른 노드로 이동하는 거리가 더 짧은 경우 
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q,(cost,i[0]))


#다익스트라 알고리즘 수행 
dijkstra(C)
cntCity = 0 
cntDist = 0 

maxDist = 0

print(distance)
#모든 노드로 가기 위한 최단 거리를 출력
for i in range(1,N+1):
    #도달할 수 없는 경우, 무한(INFINITY)이라고 출력
    if distance[i] != INF and i!=C:
        cntCity+=1
        maxDist = max(maxDist,distance[i])
        cntDist+=distance[i]

#print(cntCity,cntDist,sep=' ')
print(cntCity,maxDist,sep=' ')

        

