#프로그래머스 
#고득점 Kit
#dp
#level3
#N으로 표현

N =5
number = 12

import math

def add_repeat_num(num,k):
    rst = ''
    for i in range(k):
        rst+=str(num)
    return int(rst)

def solution(N, number):
    answer = 1
    #index -> 숫자 갯수, dp[index] -> index개로 만들 수 있는 숫자들 
    dp=[set() for _ in range(9)]
    
    while True:
        dp[answer].add(add_repeat_num(N,answer))
        # 답 체크(탈출조건1)
        if number in dp[answer]:
            break
        answer += 1
        # 탈출조건2
        if answer > 8:
            answer = -1
            break
        # make new numbers 
        for i in range(1,answer):
            for a in dp[i]:
                for b in dp[answer-i]:
                    #순서 상관 없는 연산 : +, *
                    dp[answer].add(a+b)
                    dp[answer].add(a*b)
                    #순서 상관 있는 연산 : //,- 
                    if b!=0:
                        dp[answer].add(a//b)
                    if a!=0:
                        dp[answer].add(b//a)
                    dp[answer].add(a-b)
                    dp[answer].add(b-a)

    return answer

solution(N,number)