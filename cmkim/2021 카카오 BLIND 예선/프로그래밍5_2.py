from collections import deque


def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]


def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b


def bfs(line, v, visited):
    queue = deque([v])
    visited[v] = 1

    while (queue):
        v = queue.popleft()  # 시작 기준이 되는 값을 잡고 시작한다.

        for i in range(len(line)):  # 기준값 주변에 있는 방문하지 않은 값들을 전부 탐색한다.
            if line[i][0] == v:
                for j in range(len(line)):
                    if line[j][0] == line[i][1]:
                        e = line[j][1]
                        line.append((v, e, line[i][2]+line[j][2]))
                        # if line[i][2]+line[j][2] > 0:
                        #     queue.append(e)

        for i in range(len(line)):
            print(line[i])

def solution(info, edges):
    line = []
    answer = 0
    v = len(info)
    e = len(edges)
    parent = [0] * (v + 1)

    for i in range(1, v + 1):
        parent[i] = i

    for i in range(e):
        a, b = edges[i][0], edges[i][1]
        if a == 0:
            cost = 1.01
        else:
            cost = 0
        if info[b]:  # 늑대
            cost += -1
        else:
            cost += 1.01
        line.append((a, b, cost))
    for i in range(len(edges)):
        print(line[i])

    # for edge in line:
    #     cost, a, b = edge
    #
    #     if find_parent(parent, a) != find_parent(parent, b):
    #         union_parent(parent, a, b)
    #         result += cost

    visited = [0] * len(info)
    bfs(line, 0, visited)
