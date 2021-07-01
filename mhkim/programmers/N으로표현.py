"""
@file N으로표현.py
@brief 동적계획법 - Level 3
@desc 
1번 사용한 케이스, 2번 사용한 케이스
3번 사용한 케이스 -> 1번과 2번 연산 / 2번과 1번 연산
4번 -> 1번과 3번, 2번과 2번, 3번과 1번 ... 8번까지

구할 수 있는 케이스를 구하고 찾고자 하는 값이 그 케이스들에 존재하는지 확인
"""

# Ver1. 연산 전체
def solution(N, number):
    dp = [[]]

    x = 0
    for i in range(1, 9):
        dp.append(set())
        x = 10*x + N
        dp[i].add(x)  # N, NN, NNN...

        for j in range(i):
            # 연산자 케이스
            for op1 in dp[j]:
                for op2 in dp[i-j]:
                    dp[i].add(op1 + op2)
                    dp[i].add(op1 - op2)
                    dp[i].add(op1 * op2)
                    if op2 != 0:
                        dp[i].add(op1 // op2)

            if number in dp[i]:
                return i

    return -1

# Ver2. 반만 연산
def solution(N, number):
    dp = [[]]
    
    x = 0
    for i in range(1, 9):
        dp.append(set())
        x = 10 * x + N
        dp[i].add(x) # N, NN, NNN...
        
        for j in range((i//2)+1):
            # 연산자 케이스 
            for op1 in dp[j]:
                for op2 in dp[i-j]:
                    dp[i].add(op1 + op2)
                    dp[i].add(op1 - op2)
                    dp[i].add(op2 - op1)
                    dp[i].add(op1 * op2)
                    if op1 != 0:
                        dp[i].add(op2 // op1)
                    if op2 != 0:
                        dp[i].add(op1 // op2)
                    
            if number in dp[i]:
                return i
            
    return -1