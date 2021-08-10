#solved.ac
#실버3
#구현
#도로와 신호등
#2980

from collections import deque

#신호등 개수 , 도로의 길이 
N, L = map(int,input().split())

sec = 0 
sangen = 0
# 시간 총 합
info = deque([[] for _ in range(N)])

#신호등 위치, 빨간불 시간, 초록불 시간 
for i in range(N):
    D,R,G = map(int,input().split())
    info[i].append(D)
    info[i].append(R)
    info[i].append(G)

while True:
    #신호등이 남아 있을 경우 
    if len(info)!=0:
        #신호등 위치에 상근이가 있을 경우 
        if info[0][0] == sangen:
            #빨간불+초록불
            length = info[0][1]+info[0][2]
            #빨간불인 경우 
            if (sec%length)<info[0][1]:
                sec+=(info[0][1]-(sec%length))
            #초록불인 경우 
            else:
                #이동 
                info.popleft()
                sangen+=1
                sec+=1

        else:
            if info[0][0] < L:
                sec+= info[0][0]-sangen
                sangen= info[0][0]
            else: 
                sec += (L-sangen)
        
    else:
        #도착지점까지 점프 
        sec+=(L-sangen)
        break
    #도착지점 도착시 
    if sangen==L:
        break

print(sec)
    

    
    
