n = int(input())
k = int(input())

arr = [[0]*n for _ in range(n+1)]
order = []
count = 0
dir = 0

for i in range(k):
    a, b = map(int, input().split())
    arr[a][b] = 1

l = int(input())

for i in range(l):
    # x = int(input().split())
    # c = input()
    x, c = input().split()
    order.append((int(x), c))

# for i in range(n):
#     print(arr[i])
# print(order)
# order.pop()
#print(order)

#오른쪽 볼때 좌, 우 회전 순서는 각각 우 상 좌 하 / 우 하 좌 상
#왼쪽 ''                           좌 하 우 상 / 좌 상 우 하

dx = [0, -1, 0, 1] #우 상 좌 하
dy = [1, 0, -1, 0]

x, y = 1, 1
q = [(x, y)]

while True:
    count += 1

    arr[x][y] = 2



    nx = x + dx[dir]
    ny = y + dy[dir]

    if 1 <= nx <= n and 1 <= ny <= n and arr[nx][ny] != 2:
        if arr[nx][ny] == 0:
            arr[nx][ny] = 2
            q.append((nx, ny))
            ex, ey = q.pop(0)
            arr[ex][ey] = 0

        elif arr[nx][ny] == 1:
            arr[nx][ny] = 2
            q.append((nx, ny))

        x, y = nx, ny

    else:
        break

    if count == order[0][0]:
        if order[0][1] == 'L': #왼쪽회전
            dir = (dir+1) % 4
        else:                  #오른쪽회전
            dir = (dir+3) % 4

        order.pop()

print(count)










'''
6
3
3 4
2 5
5 3
3
3 D
15 L
17  D
'''