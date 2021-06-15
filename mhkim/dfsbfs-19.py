"""
@file dfsbfs-19.py
@brief 연산자 끼워넣기
@desc dfs
"""

INF = int(1e9)+1

n = int(input())
numbers = list(map(int, input().split()))
ops = list(map(int, input().split()))  # +,-,*,/

maxVal = -INF
minVal = INF


def dfs(cnt, hap, ops):
    global maxVal
    global minVal

    if cnt == n:
        maxVal = max(hap, maxVal)
        minVal = min(hap, minVal)
        return

    if ops[0] > 0:
        ops[0] -= 1
        dfs(cnt+1, hap+numbers[cnt], ops)
        ops[0] += 1

    if ops[1] > 0:
        ops[1] -= 1
        dfs(cnt+1, hap-numbers[cnt], ops)
        ops[1] += 1

    if ops[2] > 0:
        ops[2] -= 1
        dfs(cnt+1, hap*numbers[cnt], ops)
        ops[2] += 1

    if ops[3] > 0:
        ops[3] -= 1
        if hap < 0:
            dfs(cnt+1, -(-hap//numbers[cnt]), ops)
        else:
            dfs(cnt+1, hap//numbers[cnt], ops)
        ops[3] += 1


dfs(1, numbers[0], ops)

print(maxVal)
print(minVal)
