"""
@file dfsbfs-20.py
@brief 감시 피하기
@desc
선생과 학생을 제외한 빈 곳 중에서 3곳을 선택하여 벽을 세우고
각 선생이 학생을 감시할 수 있는지 체크 - 네 방향으로 탐색
"""

from itertools import combinations as cb

N = int(input())
graph = [input().split() for _ in range(N)]

dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]

# 빈 곳 좌표
empty = []
# 선생님 좌표
teachers = []

for i in range(N):
    for j in range(N):
        if graph[i][j] == 'X':
            empty.append((i, j))
        elif graph[i][j] == 'T':
            teachers.append((i, j))


def search():
    for t in teachers:
        for i in range(4):
            nx, ny = t
            while 1:
                nx += dx[i]
                ny += dy[i]

                if nx < 0 or nx > N-1 or ny < 0 or ny > N-1 or graph[nx][ny] == 'O':
                    break

                if graph[nx][ny] == 'S':
                    return False

    return True


answer = 0
# 벽 3개 뽑은 경우의 수
for walls in cb(empty, 3):

    # 벽 만들기
    for x, y in walls:
        graph[x][y] = 'O'

    # 탐색
    if search():
        answer = 1
        break

    for x, y in walls:
        graph[x][y] = 'X'

if answer == 1:
    print('YES')
else:
    print('NO')
