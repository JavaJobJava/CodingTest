# -*- coding: utf-8 -*-
# UTF-8 encoding when using korean
n, k = map(int, input().split())
arr = list(map(int, input().split()))

min = 1000000
index = 0

for i in range(n):
    if min > arr[i]:
        min = arr[i]
        index = i

result = (n-1) //(k-1)
if (n-1) % (k-1) != 0:
    result += 1

print(result)
