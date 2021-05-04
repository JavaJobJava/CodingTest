#solved.ac
#골드2
#다익스트라
#달빛 여우
#16118
import heapq
import sys 
input = sys.stdin.readline

INF = int(1e9)
#나무 그루터기 개수, 오솔길 개수
N,M = map(int,input().split())
graph = [[] for _ in range(N+1)]
#fox, wolf 
distance_fox = [INF for _ in range(N+1)]
distance_wolf = [[INF,INF] for _ in range(N+1)]



def make_graph():
    for _ in range(M):
        x,y,c = map(int,input().split())
        graph[x].append((y,c))
        graph[y].append((x,c))

def solution():
    cnt = 0
    #달빛여우가 빠른 경우 카운팅
    for i in range(2,N+1):
        cnt = cnt+1 if distance_fox[i] < min(distance_wolf[i][0],distance_wolf[i][1]) else cnt
    return cnt

def dijkstra_fox(start):
    q = []
    #시작 노드에 대하여 초기화 ( 시작노드 데이터를 큐에 삽입)
    heapq.heappush(q,(0,start))
    distance_fox[start] = 0
    while q: #큐가 비어있지 않다면
        # 가장 최단 거리가 짧은 노드에 대한 정보 꺼내기 
        dist, now = heapq.heappop(q)
        #현재 노드가 이미 처리된 적이 있는 노드라면 무시
        if distance_fox[now] < dist:
            continue
        #현재 노드와 연결된 다른 입접한 노드들을 확인
        for i in graph[now]:
            cost = dist + i[1]
            #현재 노드를 거쳐서, 다른 노드로 이동하는 거리가 더 짧은 경우 
            if cost < distance_fox[i[0]]:
                distance_fox[i[0]] = cost
                heapq.heappush(q,(cost,i[0]))

def dijkstra_wolf(start):
    q = []
    #시작 노드에 대하여 초기화 ( 시작노드 데이터를 큐에 삽입) => (비용,노드,이동 횟수)
    heapq.heappush(q,(0,start,0))
    #0이면 빠른속도로 온거 
    #1이면 느린속도로 온거
    #1번 노드는 사실 초기화 필요 없음.
    distance_wolf[start][0]=INF
    while q: #큐가 비어있지 않다면
        # 가장 최단 거리가 짧은 노드에 대한 정보 꺼내기 
        dist, now, moves = heapq.heappop(q)
        #현재 노드가 이미 처리된 적이 있는 노드라면 무시
        if distance_wolf[now][(moves)%2] < dist:
            continue
        #현재 노드와 연결된 다른 입접한 노드들을 확인
        for i in graph[now]:
            cost = dist + i[1]/2 if moves%2==0 else dist + i[1]*2
            #현재 노드를 거쳐서, 다른 노드로 이동하는 거리가 더 짧은 경우 
            if cost < distance_wolf[i[0]][(moves+1)%2]:
                distance_wolf[i[0]][(moves+1)%2] = cost
                heapq.heappush(q,(cost,i[0],moves+1))

if __name__ == '__main__':   
    make_graph()
    dijkstra_fox(1)
    dijkstra_wolf(1)
    print(solution())
