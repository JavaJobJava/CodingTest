"""
@file 10-2.py
@brief 팀 결성
@desc 서로소 집합 알고리즘
"""

# 팀 합치기
def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b


# 같은 팀 여부 확인
def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]


n, m = map(int, input().split())
parent = [0] * (n + 1)

for i in range(0, n + 1):
    parent[i] = i

for i in range(m):
    op, a, b = map(int, input().split())
    if op == 0:
        union_parent(parent, a, b)
    elif op == 1:
        if find_parent(parent, a) == find_parent(parent, b):
            print("YES")
        else:
            print("NO")
