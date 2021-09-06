from itertools import permutations
import math

def solution(numbers):
    answer = 0

    arr = list(numbers)
    for i in range(2, len(numbers) + 1):
        pm = list(permutations(numbers, i))
        for j in pm:
            if len(j) <= len(numbers):
                arr.append(''.join(j))


    # arr = list(set(arr))
    # print(arr)

    arr = list(set([int(x) for x in arr]))
    #print(arr)

    for i in arr:
        if check(i):
            answer += 1

    return answer

def check(n):
    k = math.sqrt(n)
    if n < 2:
        return False

    for i in range(2, int(k)+1):
        if n % i == 0:
            return False
    return True