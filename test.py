import sys

input = sys.stdin.readline

while True:
    try:
        a, b, c = map(int, input().split())
        result = max(b-a, c-b)-1
        print(result)
    except :

        print('a, b, c = ', a, b, c)
        break
