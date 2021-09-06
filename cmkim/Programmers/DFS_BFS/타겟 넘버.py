from _collections import deque


def solution(numbers, target):
    answer = 0

    q = deque()
    q.append((0, 0))

    while q:
        value, index = q.popleft()

        #print('value, index = ', value, index)

        if index == len(numbers):
            if value == target:
                answer += 1

        else:
            temp = numbers[index]
            q.append((value + temp, index + 1))
            q.append((value - temp, index + 1))

    return answer


#print(solution([1, 1, 1, 1, 1], 3))
