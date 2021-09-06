
k = int(input())
n = int(input())



start = list(map(chr, range(65, 65+k)))
mid = []
end = []
end = list(map(str, input().strip()))

arr = []

for i in range(n):
    temp = list(map(str, input().strip()))
    if temp[0] == '?':
        q_mark = i
    arr.append(temp)


# for i in range(n):
#     print(arr[i])

for i in range(0, q_mark):
    for j in range(k-1):
        if arr[i][j] == '-':
            tempc = start[j]
            start[j] = start[j+1]
            start[j+1] = tempc

for i in range(n-1, q_mark, -1):
    for j in range(k-1):
        if arr[i][j] == '-':
            tempc = end[j]
            end[j] = end[j+1]
            end[j+1] = tempc

# print(start)
# print(end)

for i in range(k-1):
    if start[i] != end[i]:
        if start[i] == end[i+1] and start[i+1] == end[i]:
            mid.append('-')
            tempc = start[i]
            start[i] = start[i + 1]
            start[i + 1] = tempc
        else:
            for finish in range(k-1):
                print('x', end='')

            quit()
    else:
        mid.append('*')

for i in range(k-1):
    print(mid[i], end='')