#solved.ac
#실버3
#그래프 이론
#바이러스
#2606

#연결되어있는 애들은 다 감염! 
#1번과 연결되어있는 컴퓨터 수 구하기 
# 첫번 째 줄 : 컴퓨터 수
# 두번 째 줄 : 네트워크 연결 쌍 ex ) 1 2
# 세번 째 줄 : 연결쌍 값들 

#깊이 우선 탐색으로 
#연결된 노드 정보가 저장된 인접 리스트를 순회 
#방문을 할때 1을 더함

from sys import stdin
input = stdin.readline

N = int(input())
K = int(input())

linked= [[] for _ in range(N+1)]
visited = [False] * (N+1)

for i in range(K):
    tmp = list(map(int,input().split()))
    linked[tmp[0]].append(tmp[1])
    linked[tmp[1]].append(tmp[0])

#하고 안하고 차이는? 
for i in range(N):
    linked[i].sort()

def dfs(linked,node,visited):
    cnt = 0
    for i in linked[node]:
        #방문 처리
        if visited[i] is not True:
            visited[i] = True
            cnt += 1
            cnt += dfs(linked,i,visited)
        else:
            pass 
    
    return cnt
#1 컴퓨터 방문 처리
visited[1] = True

print(dfs(linked,1,visited))





