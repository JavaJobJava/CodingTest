arr = []
arr.append(list(map(int, input().rstrip())))

count = 0
temp = arr[0][0]

for i in range(len(arr[0])):
    if temp != arr[0][i]:
        temp = arr[0][i]
        count += 1

print(count//2)