#프로그래머스 
#고득점 Kit
#힙
#level3
#디스크 컨트롤러

# 아이디어
# request_time 오름차순 heapq인 jobs와 running_time 오름차순 heapq인 q를 생성 
# 수행할 수 있는 프로세스 중 runnin_time이 빠른 프로세스를 수행-> 기다리는 시간 최소화
# 수행할 수 있는 프로세스가 없으면 request_time이 가장 작은 프로세스들을 큐에 push  

import heapq

def solution(jobs):
    answer = 0
    cur_time = 0
    length = len(jobs)
    heapq.heapify(jobs)
    q = []
    while jobs or q:
        # 현재 진행할 수 있는 프로세스 큐에 담음.
        while jobs and jobs[0][0]<=cur_time:
            request_time, running_time = heapq.heappop(jobs)
            heapq.heappush(q,(running_time,request_time))
        # 현재 진행할 수 있는 프로세스가 있는 경우 
        if q:
            running_time, request_time =heapq.heappop(q)
            if cur_time>request_time:
                answer+=(cur_time-request_time)+running_time
                cur_time += running_time
            # cur_time <= request_time
            else:
                answer+=running_time
                cur_time = request_time+running_time
        # 현재 진행할 수 있는 프로세스가 없는 경우 
        else: 
            request_time, running_time =heapq.heappop(jobs)
            heapq.heappush(q,(running_time,request_time))
            cur_request_time = request_time
            # 요청시간이 같은 경우가 2개 이상일 때 추가적으로 뽑음 
            while jobs and jobs[0][0]==cur_request_time:
                request_time, running_time =heapq.heappop(jobs)
                heapq.heappush(q,(running_time,request_time))
    return answer//length