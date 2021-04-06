arr = []
arr.append(list(map(int, list(input().rstrip()))))

n = len(arr[0])

result = max(arr[0][0] + arr[0][1], arr[0][0] * arr[0][1]) 

for i in range(2, n):
    if arr[0][i] == 0 or arr[0][i] == 1:
        result += arr[0][i]
    else:
        result *= arr[0][i]

print(result)