# https://programmers.co.kr/learn/courses/30/lessons/42891
import copy


def solution(food_times, k):
    answer = 0
    arr = []
    arr2 = []
    arr = copy.deepcopy(food_times)
    cost = [0] * len(arr)
    accumulate_cost = [0] * len(arr)

    arr.sort()

    cur = 0
    count = 0
    sum = 0

    for i in range(len(arr)):
        if cur != arr[i]:
            cost[i] = (len(arr) - count) * (arr[i] - sum)
            cur = arr[i]
            sum = cur
            for j in range(i, len(arr)):
                if arr[i] == arr[j]:
                    count += 1

    # print(cost)

    accumulate_cost[0] = cost[0]
    for i in range(1, len(arr)):
        accumulate_cost[i] = accumulate_cost[i - 1] + cost[i]
        maxac = accumulate_cost[i]
    # print(accumulate_cost)

    n = 0
    for i in range(len(arr)):
        n = accumulate_cost[i]
        if n > k:
            # print('i = ', i)
            n = arr[i - 1]
            m = k - accumulate_cost[i - 1]
            break
    # print('k = ',k)
    # print('maxac = ', maxac)

    if k >= maxac:
        # print('Overflow')
        return -1

    #    m = k - accumulate_cost[n]

    # print('n = ' , n)
    # print('m = ' , m)

    # print(food_times)

    cnt = 0
    for i in range(len(arr)):
        if food_times[i] > n:
            arr2.append(food_times[i])

    length = len(arr2)

    for i in range(len(arr)):
        if food_times[i] > n:
            m %= length
            # print('cnt = ', cnt)
            # print('foodtimes = ', food_times[i])
            if length >= m:
                if cnt == m:
                    # print('i = ', i)
                    answer = i + 1
                    break
                cnt += 1

    # print(answer)

    return answer