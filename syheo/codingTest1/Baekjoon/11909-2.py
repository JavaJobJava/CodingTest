#solved.ac
#골드5
#다익스트라
#배열 탈출
#11909
import sys,heapq
input=sys.stdin.readline

n = int(input())
maps = []
#배열 입력 
for i in range(n):
    maps.append(list(map(int,input().split())))
#비용 초기화
INF = int(1e9)
cost = [[INF]*n for _ in range(n)]

def dijkstra():
    q=[]
    #담을 리스트 q와 위치까지 드는 최소 비용, 그리고 위치 
    heapq.heappush(q,(0,(0,0)))
    moves = [(1,0),(0,1)]
    cost[0][0] = 0
    while q: 
        # 가장 최단 거리가 짧은 노드에 대한 정보 꺼내기 
        dist, now = heapq.heappop(q)
        #현재 노드가 이미 처리된 적이 있는 노드라면 무시
        if cost[now[0]][now[1]] < dist:
            continue
        #현재 노드와 연결된 다른 입접한 노드들을 확인
        for move in moves:
            row = now[0]+move[0]
            col = now[1]+move[1]
            #이동할 수 없는 경우
            if row ==n or col==n:
                continue
            hap = dist
            #제약 조건 확인 후 계산 
            if maps[row][col]>=maps[now[0]][now[1]]:
                hap+=maps[row][col]-maps[now[0]][now[1]]+1
            #지금 노드를 거쳐서 가는게 더 효율적인 경우 
            if hap < cost[row][col]:
                cost[row][col] = hap
                heapq.heappush(q,(hap,(row,col)))
    print(cost[n-1][n-1])        

dijkstra()

