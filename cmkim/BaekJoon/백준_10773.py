k = int(input())
arr = []

for i in range(k):
    a = int(input())
    if a == 0:
        arr.pop()
    else:
        arr.append(a)

print(sum(arr))