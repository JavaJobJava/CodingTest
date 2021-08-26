arr = input()
n = len(arr)
light = [-1]
count = 0
for i in range(n):
    if arr[i] == 'Y':
        light.append(1)
    else:
        light.append(-1)

for i in range(1, n+1):
    if light[i] == 1:
        for j in range(i, n+1, i):
            light[j] *= -1
        count += 1

print(count)