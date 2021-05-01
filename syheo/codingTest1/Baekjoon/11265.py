#solved.ac
#실버1
#플로이드 와샬
#끝나지 않은 파티
#11265

'''
5 10
0 4 4 8 7
7 0 7 7 4
1 4 0 5 4
5 2 2 0 7
1 4 1 6 0
1 3 8
2 4 1
4 1 1
1 5 5
3 2 1
3 2 5
4 5 10
5 3 2
1 4 1
1 4 11
'''
#플로이드 워셜로 풀이
#플로이드 워셜은 a -> b로 갈떄 
#k라는 다른 경유지를 거쳤을 때를 모두 계산하는 방법임.
#모든 a->b 경로에 대해 모든 k의 경우를 모두 계산
#시간 복잡도 O(N^3)
import sys 
input = sys.stdin.readline

N,M = map(int,input().split())
#경로 맵 입력 
maps = []
for i in range(N):
    maps.append(list(map(int,input().split())))

#플로이드 워셜 (경유지와 도착지, 경유지와 현위치, 도착지와 현위치가 같을 경우 배제)
def floyd_warshall(N):
    for k in range(0,N):
        for a in range(0,N):
            if a==k: continue
            for b in range(0,N):
                if a==b or b==k: continue
                maps[a][b] = min(maps[a][b],maps[a][k]+maps[k][b])

floyd_warshall(N)

#정보 입력 (a->b,c:시간)
for i in range(M):
    a,b,c = map(int,input().split())
    #도착 가능 여부 검사 
    if maps[a-1][b-1]<=c:
        print('Enjoy other party')
    else:
        print('Stay here')