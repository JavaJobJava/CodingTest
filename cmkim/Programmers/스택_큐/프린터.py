from _collections import deque


def solution(priorities, location):
    answer = 0

    q = deque()
    result = deque()

    for i in range(len(priorities)):
        q.append((priorities[i], i))  # 우선 순위랑 인덱스 순서로 넣어준다

    print(q)

    while q:
        pri, index = q.popleft()
        flag = 0
        #print('pri, index = ', pri, index)
        for i in range(len(q)):
            if q[i][0] > pri:
                #print('if')
                q.append((pri, index))
                flag = 1
                break
        if flag == 0:
            result.append((pri, index))
    #print('i = ', i, q)

    #print(result)

    for i in range(len(result)):
        if result[i][1] == location:
            answer = i + 1

    return answer