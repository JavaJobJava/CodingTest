n, m = map(int, input().split()) # n이 가로, m이 세로 , 가로, 세로 순으로 받는다

arr = [[-1] * n for _ in range(m)]

screen = [0] * m
start =[0] * n
sindex = 0
for i in range(m):
    screen[i] = input()

for i in range(m):
    for j in range(n):
        if screen[i][j] == 'c':
            arr[i][j] = 0
            start[sindex] = j
            sindex += 1
        elif screen[i][j] == '.':
            arr[i][j] = 0
#print(arr)

for i in range(m):
    for j in range(n):
        if screen[i][j] == 'c':
            continue
        elif screen[i][j] == '.':





'''
4 5
c.xc
....
xx..
...x
x..x
'''