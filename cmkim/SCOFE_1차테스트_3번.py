n = int(input())
arr = [[0]*n for _ in range(n)]
dp = [0]*n

for i in range(n):
    num = int(input())
    for j in range(n):
        arr[i][j] = num // (10 ** (n - j - 1))
        num -= arr[i][j] * (10 ** (n - j - 1))

for size in range(1, n):
    for i in range(0, n - size + 1):
        for j in range(0, n - size + 1): #시작점 지정
            for k in range(0, size):
                for l in range(0, size):
                    if not arr[i+k][j+l]:
                        



