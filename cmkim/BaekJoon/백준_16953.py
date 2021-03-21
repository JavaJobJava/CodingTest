import sys
input = sys.stdin.readline

a, b = map(int, input().split())
count = 0

while b >= a:
    #print('a, b = ', a, b)
    if b % 10 == 1:
        b = b//10
    elif b % 2 == 0:
        b = b//2
    else:
        count = -1
        break
    count += 1

    if a == b:
        count += 1
        break
    elif b < a:
        count = -1
        break

print(count)