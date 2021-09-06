import sys

input = sys.stdin.readline
n = int(input())

ball = []
answer = [0] * n
color = [0] * 200001  # [0 for _ in range(200000)] #

for i in range(n):
    c, s = map(int, input().split())
    ball.append([i, c, s])

# print(ball)
ball.sort(key=lambda x: x[2])  # 사이즈, 컬러 순 오름차순
# print(ball)

j = 0
sum = 0
for i in range(n):
    a = ball[i]
    b = ball[j]

    while b[2] < a[2]:
        sum += b[2]
        color[b[1]] += b[2]
        j += 1
        b = ball[j]

    answer[a[0]] = sum - color[a[1]]

for i in range(n):
    print(answer[i])
