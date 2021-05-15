from collections import deque


def solution(t, r):
    q = []
    wait = []
    answer = []
    flag = 0
    for j in range(len(t)):
        q.append((j, int(t[j]), int(r[j])))  # id, 나갈시간, 우선순위

    for i in range(10000):
        for j in range(len(q)):
            if i == q[j][1]:
                wait.append((q[j][0], q[j][2]))

        index = 6
        for k in range(len(wait)):
            index = min(index, wait[k][1])

        for k in range(len(wait)):
            if wait[k][1] == index:
                pop_id = k
                answer.append(wait[k][0])
                wait.pop(pop_id)
                break

        flag = 0
    print(answer)

    return answer
t = [0,1,3,0]
r = [0,1,2,3]
solution(t, r)