#4.0 3.0 2.1 4.3 5.0
#2 3
#WYO
#YYO
#ABC
#DCE
#W 다본거
#O 다 못봄
#Y 보지도 않음.

import heapq

starList = list(map(float,input().split()))

row,col = map(int,input().split())
userInfo = []
for i in range(row):
    userInfo.append(list(input()))
movieInfo = []
for i in range(row):
    movieInfo.append(list(input()))

result1 = []
result2 = []
#1번 우선순위
for i in range(row):
    for j in range(col):
        if userInfo[i][j]=='Y':
            heapq.heappush(result1,(-starList[ord(movieInfo[i][j])-ord('A')],movieInfo[i][j],i,j))
        if userInfo[i][j]=='O':
            heapq.heappush(result2,(-starList[ord(movieInfo[i][j])-ord('A')],movieInfo[i][j],i,j))
#print(result1)
for i in range(len(result1)):
    result=heapq.heappop(result1)
    print(result[1],-result[0],result[2],result[3])
for i in range(len(result2)):
    result=heapq.heappop(result2)
    print(result[1],-result[0],result[2],result[3])
