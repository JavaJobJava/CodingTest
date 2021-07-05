"""
@file 타겟넘버.py
@brief DFS/BFS - Level 2
@desc dfs로 풀었지만 bfs, 순열조합 등 다른 풀이로도 가능
"""


def dfs(numbers, target, num, depth):
    if depth == len(numbers):
        if num == target:
            return 1
        return 0
    
    return dfs(numbers, target, num-numbers[depth], depth+1) + dfs(numbers, target, num+numbers[depth], depth+1)

def solution(numbers, target):
    answer = 0
    
    answer = dfs(numbers, target, (-1)*numbers[0], 1) + dfs(numbers, target, numbers[0], 1)
    
    return answer