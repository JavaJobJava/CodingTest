def solution(numbers):
    answer = ''

    num = list(map(str, numbers))
    num.sort(key=lambda x: x*3, reverse=True)



    for i in range(len(num)):
        answer += num[i]

    zero_flag = 0
    for i in range(len(answer)):
        if answer[i] != '0':
            zero_flag = 1

    if zero_flag == 0:
        return '0'

    return answer
