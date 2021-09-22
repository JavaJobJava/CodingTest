def solution(student, k):
    answer = 0

    size = len(student)
    a, b = 0, 1

    while a < size and b < size+1:
        num = 0  # 재학생 수
        flag = 0
        left = 0
        for i in range(a, b):
            if student[i]:
                num += 1
                flag = 1
            if not flag:
                left += 1

        if num == k:
            answer += (left + 1)
            b += 1


        elif num < k:
            b += 1
        elif num > k:
            a += 1

    return answer

