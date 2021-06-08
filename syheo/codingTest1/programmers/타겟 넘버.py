#프로그래머스 
#고득점 Kit
#bfs/dfs
#level3
#타겟 넘버

from collections import deque

def bfs(numbers,target):
    rst = 0
    q = [(numbers[0],1),(-numbers[0],1)]
    q = deque(q)
    while q:
        num, cnt = q.popleft()
        if cnt == len(numbers):
            if target==num:
                rst +=1
        else:
            q.append((num+numbers[cnt],cnt+1))
            q.append((num-numbers[cnt],cnt+1))
    return rst

def solution(numbers, target):
    answer = bfs(numbers,target)
    return answer