
N = int(input())
graph = []
for i in range(N):
    graph.append(list(input()))

total = 0 
size=[0 for _ in range(N+1)]
maxI=0
def visit(i,j,n):
    cnt = 0
    for x in range(i,i+n):
        for y in range(j,j+n):
            if graph[x][y]=='1':
                cnt+=1
    if cnt==n**2:
        return 1
    return 0

for i in range(1,N+1):
    for x in range(0,N-i+1):
        for y in range(0,N-i+1):
            size[i]+=visit(x,y,i)
    total+=size[i]
    maxI=i
    if size[i]==0:
        maxI=i-1
        break

print('total: %d'%(total))
for i in range(1,maxI+1):
    print('size[%d]: %d'%(i,size[i]))
