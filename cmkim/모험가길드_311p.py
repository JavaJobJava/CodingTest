n = int(input())
arr = list(map(int, input().split()))
arr.sort()

result = 0
max = 0

for i in arr:
    max += 1
    if max == i:
        result += 1
        max = 0

print(result)