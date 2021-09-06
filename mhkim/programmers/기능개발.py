from collections import deque
import math

def solution(progresses, speeds):
    answer = []
    q = deque()
    
    length = len(progresses)
    for i in range(length):
        q.append(math.ceil((100-progresses[i])/speeds[i]))

    tmp = q.popleft()
    cnt = 1
    while q:
        if tmp < q[0]:
            answer.append(cnt)
            tmp = q.popleft()
            cnt = 1
        else:
            q.popleft()
            cnt += 1
    answer.append(cnt)
    
    return answer