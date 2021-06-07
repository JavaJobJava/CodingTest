places = [["POOOP", "OXXOX", "OPXPX", "OOXOX", "POXXP"], ["POOPX", "OXPXP", "PXXXO", "OXXXO", "OOOPP"], ["PXOPX", "OXOXP", "OXPXX", "OXXXP", "POOXX"], ["OOOXX", "XOOOX", "OOOXX", "OXOOX", "OOOOO"], ["PXPXP", "XPXPX", "PXPXP", "XPXPX", "PXPXP"]]

from collections import deque

dx = [0,0,1,-1]
dy = [1,-1,0,0]

def men_distance(r1,r2,c1,c2):
    return abs(r1-c1)+abs(c2-r2)

def check_men(distance):
    if distance<=2:
        return False
    else:
        return True

def bfs(a,b,visited,maps):
    q = deque()
    q.append((a,b,0))
    visited[a][b]=True
    while q:
        row,col,dist = q.popleft()

        for i in range(4):
            r = row+dx[i]
            c = col+dy[i]
            if 0<=r<5 and 0<=c<5 and not visited[r][c] and maps[r][c]!='X':
                if maps[r][c]=='P':
                    if not check_men(dist+1):
                        return 1
                q.append((r,c,dist+1))
                visited[r][c]=True

    return 0
        


def solution(places):
    answer = []

    for place in places:
        maps = [list(map(str,list(p))) for p in place]
        cnt = 0
        for i in range(5):
            for j in range(5):
                if maps[i][j]=='P':
                    visited = [[False]*5 for k in range(5)]
                    cnt += bfs(i,j,visited,maps)
        if cnt==0:
            answer.append(1)
        else:
            answer.append(0)
                        

    return answer

print(solution(places))