# def checks(i, x):
#     if arr1[i] >= x:
#         return True
#     return False
#
#
# def checkj(i, x):
#     if h - arr1[i] + 1 <= x:
#         return True
#     return False
#
#
# def fly(x):
#     #일일히 모두체크하는 방법 시간이 오래걸린다
#     res = 0
#     for i in range(0, n // 2):
#         if checks(i, x): res += 1
#         if checkj(i, x): res += 1
#     return res
# arr1 = [[] for _ in range(n // 2)] #석순
# arr2 = [[] for _ in range(n // 2)] #종유석
# for i in range(h):
#     print(sum[i])
#print(sum)
# for i in range(n // 2):
#     arr1[i] = int(input())
#     arr2[i] = int(input())

# answer = 1e9
# for i in range(1, h):
#     crash = fly(i)
#     if crash < answer:
#         answer = crash
#         count = 1
#     elif crash == answer:
#         count += 1

n, h = map(int, input().split())
sum = [0 for _ in range(h+1)]

for i in range(n):
    bar = int(input())
    if i % 2 == 0: #석순
        sum[1] += 1
        sum[bar + 1] -= 1
    else:          #종유석
        sum[h - bar + 1] += 1

#print(sum)
answer = 1e9
for i in range(1, h+1):
    sum[i] += sum[i-1]

    if sum[i] < answer:
        answer = sum[i]
        count = 1
    elif sum[i] == answer:
        count += 1
#print(sum)
print(answer, count)