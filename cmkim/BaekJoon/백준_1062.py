n, k = map(int, input().split())

arr = []
teach = []
for i in range(n):
    arr.append(input())
# for i in range(n):
#     print(arr[i])
for i in range(n):
    teach.append(arr[i][4:-4])
# for i in range(n):
#     print(teach[i])
for i in range(n):
    teach[i] = set(teach[i])
# for i in range(n):
#     print(teach[i])