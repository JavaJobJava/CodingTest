a, b = map(int, input().split())

n = int(input())
num = 0         #A진법 수를 저장할 10진수
arr = list(map(int,input().split()))

for i in arr: ##A진법 수를 10진수로 변환해서 num에 저장
    num *= a
    num += i


index = 0
b_index = b
while b_index < num:
    index += 1
    b_index *= b

divide = 0

for i in range (index, -1, -1):
    divide = num//(b**i)
    num -= divide*(b**i)

    if divide>0:
        print(divide, end=' ')
        divide = 0
    elif divide == 0 :
        print(0, end=' ')
