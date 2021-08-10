"""
@file 순위.py
@brief 그래프 - Level 3
@desc 
플로이드 워셜 알고리즘을 생각하지 못함
"""


def floydWarshall(graph, n):
    for k in range(n+1):
        for i in range(n+1):
            for j in range(n+1):
                # i선수가 k선수를 이기고 k선수가 j선수를 이기면 i선수는 j선수를 이긴 것
                if graph[i][k] == 1 and graph[k][j] == 1:
                    graph[i][j] = 1
                # i선수가 k선수에게 지고 k선수가 j선수에게 졌으면 i선수는 j선수에게 진 것
                elif graph[i][k] == -1 and graph[k][j] == -1:
                    graph[i][j] = -1


def solution(n, results):
    winlose = [[0 for _ in range(n+1)] for _ in range(n+1)]  # 승부 모르면 0
    for w, l in results:
        # 승리 1, 패배 -1
        winlose[w][l] = 1
        winlose[l][w] = -1

    # floyd-warshall
    floydWarshall(winlose, n)

    # n-1번 대결한(플로이드 워셜 결과) 선수는 순위가 확정
    answer = 0
    for wl in winlose:
        if wl.count(-1) + wl.count(1) == n-1:
            answer += 1

    return answer
