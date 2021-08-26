g = int(input())
a, b = 1, 2 #기억한 몸무게, 현재 몸무게

find = False
while a < 50002 and b < 50002:
    if b**2 - a**2 == g:
        print(b)
        find = True
        a += 1
        b += 1
    elif (b**2 - a**2) > g:
        a += 1
    else:
        b += 1

if not find:
    print(-1)

#시간이 왜 이렇게 오래 걸리는지?