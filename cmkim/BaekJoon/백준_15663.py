from itertools import permutations

n, m = map(int, input().split())
n_list = list(map(int, input().split()))
n_list = sorted(n_list)

output = []
for numbers in list(permutations(n_list, m)):
    output.append(numbers)
output = sorted(list(set(output)))

for numbers in output:
    for num in numbers:
        print(num, end=' ')
    print('\n')
# def recur(k):
#     if k == m:
#         for i in range(k):
#             print(answer[i], end=' ')
#         print('')
#         return
#     prev = 0
#     for i in range(n):
#         if used[i]: continue
#         if k > 0 and answer[k - 1] > arr[i]: continue
#
#         if prev != arr[i]:
#             used[i] = True
#             answer[k] = arr[i]
#             prev = arr[i]
#             recur(k + 1)
#             used[i] = False
#
#
# n, m = map(int, input().split())
# used = [False for _ in range(8)]
# arr = list(map(int, input().split()))
# answer = [-1 for _ in range(m)]
# arr.sort()
# recur(0)
