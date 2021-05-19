from itertools import combinations
n, m = map(int, input().split())

arr = []
chicken = []
home = []

for i in range(n):
    temp = list(map(int, input().split()))
    for j in range(n):
        if temp[j] == 1:
            home.append((i, j))
        elif temp[j] == 2:
            chicken.append((i, j))

m_chicken = list(combinations(chicken, m))

def get_sum(candidate):
    result = 0
    for hx, hy in home:
        temp = 1e9
        for cx, cy in candidate:
            temp = min(temp, abs(hx - cx) + abs(hy - cy))
        result += temp
    return result

result = 1e9
for i in m_chicken:
    result = min(result, get_sum(i))


print(result)

'''
5 3
0 0 1 0 0
0 0 2 0 1
0 1 2 0 0
0 0 1 0 0
0 0 0 0 2
'''