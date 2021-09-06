#solved.ac
#실버5
#그리디
#병든 나이트
#1783
#이동 방법 
#2칸 위로, 1칸 오른쪽
#1칸 위로, 2칸 오른쪽
#1칸 아래로, 2칸 오른쪽
#2칸 아래로, 1칸 오른쪽
import sys
input = sys.stdin.readline
#세로와 가로 
N,M = map(int,input().split())
 
#제한 
colMax=M-1 

#이동 경우의 수 (배치가 중요함 )
moves = [(-2,1),(2,1),(-1,2),(1,2)]

#4가지 동작 후 이동 가능 여부 
if M>=7 and N>=3:
    canFourMove = True
else:
    canFourMove = False

#4가지 동작이 되지 않을 경우 
if not canFourMove:
    row = N-1
    col = 0 
    cnt = 1
    #N==2 
    if N==2: 
        if M>=7:
            cnt+=3
        elif M>=5:
            cnt +=2
        elif M>=3:
            cnt +=1
        else:
            pass
    #N>=3
    elif N>=3:
        if M==2:
            cnt+=1
        elif M==3:
            cnt+=2
        elif M>=4 and M<=6:
            cnt+=3
    
#최대한 많은곳에 방문하게 이동 카운트 증가 
if canFourMove:
    #시작 위치 
    col=6
    #방문 수
    cnt = 5
    cnt+=colMax-col
 
print(cnt)






