n, m, l = map(int, input().split())

cut = []
arr = []
for i in range(m):  # 자르는 위치
    cut.append(int(input()))
#print(cut)

for i in range(n):  # 자르는 횟수
    arr.append(int(input()))

def calculate(mid, count): # 가장 작은 조각의 길이 > mid 일때 횟수를 세서 count 값이 만들어지면 성공
    prev = 0
    for i in range(m):
        if cut[i] - prev >= mid:
            count -= 1
            prev = cut[i]
            if count == 0:
                break


    if count == 0 and l - prev >= mid:
        return True
    else:
        return False

for i in range(n):
    piece = arr[i]
    left = 0
    right = l

    while left + 1 < right:
        mid = (left + right) // 2
        if calculate(mid, piece):
            left = mid
        else:
            right = mid

    print(left)






