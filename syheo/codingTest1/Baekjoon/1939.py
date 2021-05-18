#solved.ac
#골드4
#?
#중량제한
#1939

# 첫번쨰 아이디어
# 인접 행렬로 bfs만 돌음 -> 메모리초과
# 인접 리스트로 bfs만 돌음 -> 메모리 초과
# 중량 초과하면 간선 가중치만큼 길을 통과할 수 있다고 생각함.
# 중량 초과하면 아예 가질 못함
# 두번째 아이디어 
# 중량을 이진탐색으로 선택, bfs 돌려서 갈 수 있는 경우와 못가는 경우로 left, right 조절

from collections import deque

INF = int(1e9)

def binary_search(A,B):
    answer = 0
    left = 0 
    right = INF 
    mid = (left+right)//2
    while left<=right:
        #방문 배열 초기화 
        visited = [False for _ in range(N+1)]
        if bfs(A,B,mid,visited):
            answer = max(mid,answer)
            left = mid+1
        else:
            right = mid-1
        mid = (left+right)//2
    return answer 
    
def bfs(A,B,mid,visited):
    q = deque([A]) # 섬, 비용 
    visited[A]=True
    while q:
        land = q.popleft()
        for info in graphs[land]:
            dest = info[0]
            destCost = info[1]
            #문제를 잘못 이해함 
            #c = cost if destCost>=cost else destCost
            #중량제한 통과 
            if mid<=destCost:
                #방문했던 노드가 아니면 
                if not visited[dest]:
                    visited[dest]=True
                    if dest==B:
                        return True 
                    else:
                        q.append(dest)
        
    return False

#섬 개수, 도로 갯수
N, M = map(int,input().split())
#인접 리스트 초기화 
graphs = [[] for _ in range(N+1)]
#인접 리스트 입력
for i in range(M):
    a,b,c = map(int,input().split())
    #a->b;c , b->a;c
    graphs[a].append((b,c))
    graphs[b].append((a,c))

# 공장이 있는 두 개의 섬 
A,B = map(int,input().split())

# binarySearch and bfs 
print(binary_search(A,B))
