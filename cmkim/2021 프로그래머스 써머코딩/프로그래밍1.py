import sys


# from collections import deque


def solution(code, day, data):
    answer = []
    q = []
    for i in data:
        arr = i.split(' ')
        time = []
        if code in arr[1]:
            if day in arr[2]:
                time.append(int(arr[2][5:13]))
                time.append(int(arr[2][13:15]))

                num = arr[0].split('=')
                # answer.append(int(num[1]))
                price = int(num[1])
                q.append((time[1], time[0], price))

    q.sort()

    for i in range(len(q)):
        answer.append(q[i][2])

    return answer