"""
@file 정수삼각형.py
@brief DP - Level 3
@desc 
바텀업
"""


# d[i][j] : i행 j열까지의 가장 큰 합
def solution(triangle):
    d = [[0 for j in range(i+1)] for i in range(len(triangle))]
    d[0] = triangle[0]
    for i in range(1, len(triangle)):
        for j in range(i+1):
            if j == 0:
                d[i][j] = d[i-1][j] + triangle[i][j]
            elif j == i:
                d[i][j] = d[i-1][j-1] + triangle[i][j]
            else:
                d[i][j] = max(d[i-1][j-1], d[i-1][j]) + triangle[i][j]

    return max(d[len(triangle)-1])
