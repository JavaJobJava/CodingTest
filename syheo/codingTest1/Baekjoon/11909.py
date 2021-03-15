#solved.ac
#골드5
#다익스트라
#배열 탈출
#11909

# 1≤i,j<n이라면, 상수는 A[i][j+1] 또는 A[i+1][j]로만 건너갑니다. 하 , 우 
# i=n,1≤j<n이라면, A[i][j+1]로만 건너갑니다. 우
# 1≤i<n,j=n이라면 A[i+1][j]로만 건너갑니다. 하 
# i=j=n인 경우 바로 출구로 갑니다.

import sys, heapq
input=sys.stdin.readline
INF = int(1e9)

n = int(input())
maps = []
maps.append([INF]*(n+1))
#배열 입력 
for i in range(n):
    tmp = [INF]+list(map(int,input().split()))
    maps.append(tmp)

#비용 초기화
cost = [[0]*(n+1) for _ in range(n+1)]

cost[1][1]=0
#디피 
for i in range(1,n+1):
    for j in range(1,n+1):
            if j-1==0 and i-1==0:
                continue
            elif j-1==0:
                button2 = cost[i-1][j] if maps[i][j]<maps[i-1][j] else maps[i][j]-maps[i-1][j] + 1 + cost[i-1][j]
                cost[i][j]+=button2
            elif i-1==0:
                button1 = cost[i][j-1] if maps[i][j]<maps[i][j-1] else maps[i][j]-maps[i][j-1] + 1 + cost[i][j-1]
                cost[i][j]+=button1  
            else:
                button1 = cost[i][j-1] if maps[i][j]<maps[i][j-1] else maps[i][j]-maps[i][j-1] + 1 + cost[i][j-1]
                button2 = cost[i-1][j] if maps[i][j]<maps[i-1][j] else maps[i][j]-maps[i-1][j] + 1 + cost[i-1][j]
                cost[i][j]+=min(button1,button2)
# for i in range(n+1):
#     for j in range(n+1):
#         print(cost[i][j],end=" ")
#     print('')
print(cost[n][n])   
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
     

        
