#프로그래머스 
#고득점 Kit
#스택
#level2
#기능개발

import math
def solution(progresses, speeds):
    answer = []
    days = [math.ceil((100-progresses[i])/speeds[i]) for i in range(len(progresses))]
    now = days[0]
    cnt = 1
    for i in range(1,len(days)):
        if now>=days[i]:
            cnt += 1
        else:
            now = days[i]
            answer.append(cnt)
            cnt = 1
    answer.append(cnt)
            
        
    return answer