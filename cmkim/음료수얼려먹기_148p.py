n, m = map(int, input().split()) #세로, 가로 순서


graph=[]
for i in range(n):
    graph.append(list(map(int, input())))  #graph[0][0] ~ graph[n-1][m-1] 까지 map 입력

def search(x,y):
    if x<0 or x>=n or y<0 or y>=m :
        return False

    if graph[x][y]==0:
        graph[x][y]=1
        search(x-1, y)
        search(x+1, y)
        search(x, y-1)
        search(x, y+1)
        return True #주변에 있는 0으로 이뤄진 칸 전부 탐색후 return True

    return False #0으로 이루어진 칸을 못찾을때

result = 0
for i in range(n):
    for j in range(m):
        if search(i,j):
            result+=1
print(result)

"""
15 14
00000111100000
11111101111110
11011101101110
11011101100000
11011111111111
11011111111100
11000000011111
01111111111111
00000000011111
01111111111000
00011111111000
00000001111000
11111111110011
11100011111111
11100011111111
"""