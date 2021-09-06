#프로그래머스 
#고득점 Kit
#완전 탐색
#level2
#소수 찾기

import sys
import math
sys.setrecursionlimit(10**9)
answer = set()

def isPrime(n):
    if n<2:
        return False
    for i in range(2,int(math.sqrt(n))+1):
        if n%i==0:
            return False
    return True

def dfs(numbers,visited,string,length):
    global answer
    for i in range(length):
        if not visited[i]:
            #방문 처리 
            visited[i]=True
            #소수 검사
            if isPrime(int(string+numbers[i])):
                #정답 추가 
                answer.add(int(string+numbers[i]))
            dfs(numbers,visited,string+numbers[i],length)
            #방문 undo
            visited[i]=False

def solution(numbers):
    numbers = list(numbers)
    length = len(numbers)
    visited = [False for _ in range(length)]
    dfs(numbers,visited,'',length)
    return len(answer)

