#CH13 BFSDFS기출
#예제 13-20
#감시 피하기
#백준 18428
#실버 1

from collections import deque

N = int(input())

maps = []
students = []
teachers = []
obstructs = []
for i in range(N):
    tmp = list(map(str,input().split()))
    for j in range(N):
        if tmp[j]=='S':
            students.append((i,j))
        if tmp[j]=='T':
            teachers.append((i,j))
        if tmp[j]=='X':
            obstructs.append((i,j))
    maps.append(tmp)

def isAvoid(a,b,d):
    for student in students:
        row = student[0]
        col = student[1]
        r = row
        c = col
        n = 1
        while r-n>=0:
            if (a[0]==r-n and a[1]==col) or (b[0]==r-n and b[1]==col) or (d[0]==r-n and d[1]==col):
                break
            if maps[r-n][col]=='T':
                return False
            n+=1
        n = 1
        while r+n<N:
            if (a[0]==r+n and a[1]==col) or (b[0]==r+n and b[1]==col) or (d[0]==r+n and d[1]==col):
                break
            if maps[r+n][col]=='T':
                return False
            n+=1
        n = 1
        while c-n>=0:
            if (a[0]==row and a[1]==c-n) or (b[0]==row and b[1]==c-n) or (d[0]==row and d[1]==c-n):
                break
            if maps[row][c-n]=='T':
                return False
            n+=1
        n = 1
        while c+n<N:
            if (a[0]==row and a[1]==c+n) or (b[0]==row and b[1]==c+n) or (d[0]==row and d[1]==c+n):
                break
            if maps[row][c+n]=='T':
                return False
            n+=1


    return True

def bfs():
    #visited = [[False]*N for _ in range(N)]
    q = deque([])
    #실수가 있었음 -> range 안에 len(obstructs)-2를 넣어야 하는데 N을 넣음 ;; 
    for i in range(len(obstructs)-2):
        q.append(([i],1)) #방해물 위치 인덱스, 카운트
    while q: 
        locs , cnt = q.popleft()
        if cnt == 3:
            if isAvoid(obstructs[locs[0]],obstructs[locs[1]],obstructs[locs[2]]):
                return True 
        else:
            for i in range(locs[-1]+1,len(obstructs)):
                q.append((locs+[i],cnt+1))

    return False
    
if bfs():
    print("YES")
else:
    print("NO")


