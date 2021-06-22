"""
@file dfsbfs-21.py
@brief 인구 이동
@desc
연합 찾기 - 연결된 나라 (나라마다 체크)
인구 이동 없을 때까지 반복하고 / 연합 국가끼리 인구 분배

deque는 탐색을 위한 / yeonhap은 연합인 나라 저장 공간
"""

import sys
from collections import deque

N, L, R = map(int, sys.stdin.readline().split())
A = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]


def search(x, y, num):
    # x, y와 연합인 나라
    yeonhap = []
    yeonhap.append((x, y))
    total = A[x][y]  # 연합의 전체 인구 수
    union[x][y] = num  # 연합 번호

    # BFS
    q = deque([(x, y)])
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < N and 0 <= ny < N and union[nx][ny] == -1:
                if L <= abs(A[nx][ny] - A[x][y]) <= R:
                    q.append((nx, ny))
                    yeonhap.append((nx, ny))
                    union[nx][ny] = num
                    total += A[nx][ny]

    # 인구 분배
    nCountry = len(yeonhap)
    for a, b in yeonhap:
        A[a][b] = total // nCountry


days = 0
while True:
    # 연합 초기화
    union = [[-1]*N for _ in range(N)]
    num = 0  # 연합국 번호

    # 각 나라마다 체크
    for i in range(N):
        for j in range(N):
            if union[i][j] == -1:  # 아직 처리되지 않은 나라
                search(i, j, num)
                num += 1

    # 모든 인구 이동
    if num == N * N:
        break

    days += 1

print(days)
