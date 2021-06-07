n = int(input())
arr = list(map(int, input().split()))
add, sub, mul, div = map(int, input().split())  # [+] [-] [*] [//]

min_value = 1e9
max_value = -1e9

def dfs(count, value):
    global min_value, max_value, add, sub, mul, div

    if count == n:
        min_value = min(min_value, value)
        max_value = max(max_value, value)

    else:
        if add > 0:
            add -= 1
            dfs(count + 1, value + arr[count])
            add += 1
        if sub > 0:
            sub -= 1
            dfs(count + 1, value - arr[count])
            sub += 1
        if mul > 0:
            mul -= 1
            dfs(count + 1, value * arr[count])
            mul += 1
        if div > 0:
            div -= 1
            dfs(count + 1, int(value / arr[count]))
            div += 1

dfs(1, arr[0])

print(max_value)
print(min_value)
