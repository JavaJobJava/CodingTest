#1002
#터렛

#조규현과 백승환은 터렛에 근무하는 직원이다. 하지만 워낙 존재감이 없어서 인구수는 차지하지 않는다. 다음은 조규현과 백승환의 사진이다.

#이석원은 조규현과 백승환에게 상대편 마린(류재명)의 위치를 계산하라는 명령을 내렸다. 조규현과 백승환은 각각 자신의 터렛 위치에서 현재 적까지의 거리를 계산했다.
#조규현의 좌표 (x1, y1)와 백승환의 좌표 (x2, y2)가 주어지고, 조규현이 계산한 류재명과의 거리 r1과 백승환이 계산한 류재명과의 거리 r2가 주어졌을 때,
#류재명이 있을 수 있는 좌표의 수를 출력하는 프로그램을 작성하시오.
# 한 줄에 x1, y1, r1, x2, y2, r2가 주어진다. x1, y1, x2, y2는 -10,000보다 크거나 같고, 10,000보다 작거나 같은 정수이고, 
# r1, r2는 10,000보다 작거나 같은 자연수이다.
import math 
T = int(input())
result = []
for i in range(T):
    x1, y1, r1, x2, y2, r2 = map(int,input().split())
    distance = math.sqrt((x1-x2)**2 + (y1-y2)**2)
    #원의 중심이 같을 경우 
    if x1==x2 and y1 == y2:
        if r1 == r2:
            result.append(-1)
        else:
            result.append(0)
    #원이 다른 원을 포함하는 경우 
    elif r1<r2 and (r2-distance)>=r1:
        if (r2-distance)==r1:
            result.append(1)
        else:
            result.append(0)
    elif r1>r2 and (r1-distance)>=r2:
        if (r1-distance)==r2:
            result.append(1)
        else:
            result.append(0)
    #두 원이 서로 바깥에 있는 경우 
    else:
        if r1+r2 < distance:
            result.append(0)
        elif r1+r2 > distance:
            result.append(2)
        else: result.append(1)

for i in range(T):
    print(result[i])



