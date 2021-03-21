#N,M
N,M = map(int,input().split())
maps = []
tmp = [0 for _ in range(N+1)]
maps.append(tmp)
for i in range(M):
    maps.append(list(map(int,input().split())))
    maps[i+1].insert(0,0)
#print(maps)

for i in range(1,M+1):
    for j in range(1,N+1):
        maps[i][j]+=max(maps[i-1][j],maps[i][j-1])

print(maps[M][N])