n, m = map(int, input().split())
arr = list(map(int, input().split()))
repeated = [0] * (11)
repeatedsum = 0

def nCr(x, y):
    a = 1
    b = 1
    for i in range(x, x-y, -1):
        a *= i
    for i in range(y, 0, -1):
        b *= i

    return a//b

for i in arr:
    repeated[i] += 1

for i in range(m+1):
    if repeated[i] > 1:
        repeatedsum += nCr(repeated[i], 2)

result = nCr(n, 2) - repeatedsum

print(result)

'''
5 3
1 3 2 3 2

8 5
1 5 4 3 2 4 5 2
'''