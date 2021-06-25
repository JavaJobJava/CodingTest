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
    rest = k # 남은 시간 
    length = len(food_times) 
    #k 시간 안에 현재 음식을 다먹을 수 있을 경우
    if sum(food_times)<=k:
        return -1
    
    q = []
    #(식사시간, 음식 위치)를 우선순위 큐에 넣어줌 O(logN)xN
    for i in range(length):
        heapq.heappush(q,(food_times[i],i))
    
    rotation = q[0][0] # 진행할 로테이션 횟수 
    prev_rot = 0
    #큐에 음식이 있고, 로테이션 진행 가능시 
    while rest>=len(q)*(rotation-prev_rot):  
        #남은 횟수
        rest-=(rotation-prev_rot)*len(q)
        #rotation만큼 돌릴 수 있는 음식 제거 
        while q[0][0]==rotation:
            heapq.heappop(q)
        #로테이션 갱신 
        prev_rot = rotation
        rotation = q[0][0]
        
    #음식 번호로 정렬 O(NlogN)
    q.sort(key=lambda x : x[1])
    answer = q[rest%len(q)][1]+1

    return answer