#프로그래머스 
#고득점 Kit
#힙
#level2
#더 맵게

import heapq

def solution(scoville, K):
    answer = 0
    heapq.heapify(scoville)
    answer += 1
    heapq.heappush(scoville,heapq.heappop(scoville)+2*heapq.heappop(scoville))
    while scoville[0]<K:
        if len(scoville)<2:
            return -1
        heapq.heappush(scoville,heapq.heappop(scoville)+2*heapq.heappop(scoville))
        answer+=1
    
    return answer