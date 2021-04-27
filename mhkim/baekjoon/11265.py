"""
@file 11265.py
@brief 끝나지 않는 파티
@desc 플로이드 워셜
"""
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
parties = []
for i in range(n):
    parties.append(list(map(int, input().split())))


def floyd_warshall():
    for k in range(n):
        for i in range(n):
            for j in range(n):
                parties[i][j] = min(
                    parties[i][j], parties[i][k] + parties[k][j])


floyd_warshall()

for i in range(m):
    a, b, c = map(int, input().split())
    if parties[a-1][b-1] <= c:
        print("Enjoy other party")
    else:
        print("Stay here")
