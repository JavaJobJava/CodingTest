n = int(input())

arr = []
temp = [[0] * n for _ in range(n)]
teacher = []
find = 0
for i in range(n):
    arr.append(list(map(str, input().split())))
    for j in range(n):
        if arr[i][j] == 'T':
            teacher.append((i, j))


def dfs(count):
    global find
    if count == 3:  # 장애물 3개가 다 설치된 경우
        for i in range(n):  # 장애물 설치된 맵을 복사한 후에
            for j in range(n):
                temp[i][j] = arr[i][j]

        if not check():  # 감시를 피하면 YES 출력후 종료
            print("YES")
            quit()

        else:  # 감시 못피하면 다른 경우도 검사해보기
            return

    for i in range(n):  # 빈 공간에 대해서 장애물 3개까지 설치해보는 과정
        for j in range(n):
            if arr[i][j] == 'X':
                arr[i][j] = 'O'  # 알파벳 O임
                count += 1
                dfs(count)
                count -= 1
                arr[i][j] = 'X'


def check():
    result = 0
    for x, y in teacher:
        for i in range(4):  # 상하좌우 방향 검사
            if see(x, y, i):  # 학생의 위치를 파악한 경우
                return True

    return False  # 학생의 위치를 파악하지 못한 경우


def see(x, y, dir):  # 상하좌우 순으로 검사
    if dir == 0:
        while 0 <= x < n:
            if temp[x][y] == 'S':
                return True
            if temp[x][y] == 'O':
                return False
            else:
                x -= 1
    if dir == 1:
        while 0 <= x < n:
            if temp[x][y] == 'S':
                return True
            if temp[x][y] == 'O':
                return False
            else:
                x += 1
    if dir == 2:
        while 0 <= y < n:
            if temp[x][y] == 'S':
                return True
            if temp[x][y] == 'O':
                return False
            else:
                y -= 1
    if dir == 3:
        while 0 <= y < n:
            if temp[x][y] == 'S':
                return True
            if temp[x][y] == 'O':
                return False
            else:
                y += 1

    return False


dfs(0)#dfs 함수안에서 한번만이라도 감시를 피했으면 YES 출력후 종료함
print("NO")
