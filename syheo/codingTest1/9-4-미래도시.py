#CH9 최단 경로
#예제 9-4
#미래도시

# 방문 판매원 A는 현재 1번 회사에 위치해 있으며, X번 회사에 방문해 물건을 판매
# 또한 연결된 2개의 회사는 양방향으로 이동할 수 있음.
# 거리 이동 시간은 모두 1
# 소개팅 회사 K번 
# A->K->X
import heapq

INF = int(1e9)

#N, M 
N,M = map(int,input().split())

#각 노드에 연결되어 있는 노드에 대한 정보를 담는 리스트 만들기
graph = [ [] for i in range(N+1)]
#최단 거리 테이블을 모두 무한으로 초기화
distance = [INF] * (N+1)

#모든 간선 정보를 입력받기
for _ in range(M):
    a,b = map(int, input().split())
    # a번 노드에서 b번 노드로 가는 비용이 c라는 의미
    graph[a].append((b,1))
    # 양방향 이동 가능
    graph[b].append((a,1))

X,K = map(int,input().split())

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
dijkstra(1)
Kdist = distance[K]
distance = [INF] * (N+1)
dijkstra(K)
Xdist = distance[X]

if Kdist == INF or Xdist == INF:
    print(-1)
else:
    print(Kdist+Xdist)

