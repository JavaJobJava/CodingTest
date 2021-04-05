def dfs(n, count):
    if count == 6:
        for i in range(1, k+1):
            if selected[i]:
                print(arr[i], end=' ')
        print()
        return

    for i in range(n, k+1):
        selected[i] = 1
        dfs(i+1, count+1)
        selected[i] = 0


while True:
    arr = list(map(int, input().split()))
    k = arr[0]
    selected = [0] * (k + 1)
    if k == 0:
        break

    dfs(1, 0)
    print()



