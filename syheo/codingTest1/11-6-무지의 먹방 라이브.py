#CH11 그리디 기출
#예제 11-6
#무지의 먹방 라이브
#카카오 신입 공채 2019 

#엄청 오래 걸림
#효율성 있게 하기 어려웠음.
import heapq
from collections import deque

def solution(food_times, k):
    answer = 0
    rest = k
    length = len(food_times)
    rotation = 1
    q = []
    #(식사시간, 음식 위치)를 우선순위 큐에 넣어줌 O(logN)xN
    for i in range(length):
        heapq.heappush(q,(food_times[i],i))
    while True:
        #큐에 음식이 있고, 로테이션 1회 진행 가능시 
        if  q and rest//len(q):  
            #남은 횟수
            rest-=1*len(q)
            #큐에 음식이 있고, rotation만큼 돌릴 수 있는 음식 제거 
            while q and q[0][0]==rotation:
                heapq.heappop(q)
            #로테이션 1증가 
            rotation+=1
        else:
            #음식 번호로 정렬 O(NlogN)
            q.sort(key=lambda x : x[1])
            #큐에 남은 음식이 없을 경우 
            if len(q)==0:
                answer = -1
            else:
                answer = q[rest][1]+1
            break

    return answer