#solved.ac
#골드5
#다익스트라
#배열 탈출
#11909

# 1≤i,j<n이라면, 상수는 A[i][j+1] 또는 A[i+1][j]로만 건너갑니다. 하 , 우 
# i=n,1≤j<n이라면, A[i][j+1]로만 건너갑니다. 우
# 1≤i<n,j=n이라면 A[i+1][j]로만 건너갑니다. 하 
# i=j=n인 경우 바로 출구로 갑니다.

import sys
input=sys.stdin.readline
INF = int(1e9)

n = int(input())
maps = [[INF]*(n+1)]
#배열 입력 
for i in range(n):
    maps.append([INF]+list(map(int,input().split())))

#비용 초기화
cost = [[0 for _ in range(n+1)] for _ in range(n+1)]

def cal(a,b):
    if a>b:
        return 0
    else:
        return b-a+1

#디피 
def dp():
    for i in range(1,n+1):
        for j in range(1,n+1):
                if j-1==0 and i-1==0:
                    continue
                elif j-1==0:
                    cost[i][j]+=cal(maps[i-1][j],maps[i][j]) + cost[i-1][j]
                elif i-1==0:
                    cost[i][j]+=cal(maps[i][j-1],maps[i][j]) + cost[i][j-1]  
                else:
                    cost[i][j]+=min(cal(maps[i][j-1],maps[i][j]) + cost[i][j-1],cal(maps[i-1][j],maps[i][j]) + cost[i-1][j])
    print(cost[n][n])   
dp()
# #다익스트라 실패 
# def dijkstra():
#     q=[]
#     #담을 리스트 q와 위치까지 드는 최소 비용, 그리고 위치 
#     heapq.heappush(q,(0,(0,0)))
#     moves = [(1,0),(0,1)]
#     cost[0][0] = 0
#     while q: 
#         # 가장 최단 거리가 짧은 노드에 대한 정보 꺼내기 
#         dist, now = heapq.heappop(q)
#         #현재 노드가 이미 처리된 적이 있는 노드라면 무시
#         if cost[now[0]][now[1]] < dist:
#             continue
#         #현재 노드와 연결된 다른 입접한 노드들을 확인
#         for move in moves:
#             row = now[0]+move[0]
#             col = now[1]+move[1]
#             #이동할 수 없는 경우
#             if row ==n or col==n:
#                 continue
#             button = 0
#             #제약 조건 확인 후 계산 
#             if maps[row][col]>=maps[now[0]][now[1]]:
#                 button+=maps[row][col]-maps[now[0]][now[1]]+1
#             hap=dist+button
#             #지금 노드를 거쳐서 가는게 더 효율적인 경우 
#             if hap < cost[row][col]:
#                 cost[row][col] = hap
#                 heapq.heappush(q,(hap,(row,col)))

#dijkstra()
     

        
