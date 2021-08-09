n, m = map(int, input().split())

arr = list(map(int, input().split()))

answer = 0

#완전 탐색 pypy3로만 통과
# for start in range(0, len(arr)):
#     sum = 0
#     for end in range(start, len(arr)):
#         sum += arr[end]
#         if sum == m:
#             answer += 1
#             break
#         elif sum > m:
#             break

#투포인터 방식으로는 어떻게 풀까? 고민하기
sum = 0
start = 0
for end in range(len(arr)):
    sum += arr[end]
    while sum > m:
        sum -= arr[start]
        start += 1
    if sum == m:
        answer += 1



print(answer)
