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
sum = 0
info = deque([[] for _ in range(N)])

for i in range(N):
    D,R,G = map(int,input().split())
    info[i].append(D)
    info[i].append(R)
    info[i].append(G)

while True:
    if len(info)!=0:
        if info[0][0] == sangen:
            length = info[0][1]+info[0][2]
            if (sec%length)<info[0][1]:
                pass
            else:
                info.popleft()
                sangen+=1
        else:
            sangen+=1
        sec+=1
    else:
        sec+=(L-sangen)
        break
    if sangen==L:
        break

print(sec)
    

    
    
