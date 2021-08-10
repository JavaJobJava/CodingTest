"""
@file 프린터.py
@brief 프로그래머스 스택/큐 - Level 2
@desc 
우선순위를 보고 heapq면 어떨까 했는데 heapify는 문제의 우선순위 보장을 못함
큐 2개 - 1. 우선순위 체킹 / 2. 타겟 검출
"""
from collections import deque


def solution(priorities, location):
    targetPriority = priorities[location]

    sortedPriorities = sorted(priorities, reverse=True)
    sortedQ = deque(sortedPriorities)  # 우선순위 체킹 위해서

    q = deque()
    for i in range(len(priorities)):
        q.append((priorities[i], i))

    cnt = 1
    while q:
        p, idx = map(int, q[0])

        if p < sortedQ[0]:
            q.append(q.popleft())
        else:
            if targetPriority == sortedQ[0]:
                if idx == location:
                    break
                else:
                    q.append(q.popleft())
                    cnt += 1
            else:
                cnt += 1
                q.popleft()
                sortedQ.popleft()

    return cnt
