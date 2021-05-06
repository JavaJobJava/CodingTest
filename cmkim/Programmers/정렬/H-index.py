def solution(citations):
    answer = 0
    count = 0
    length = len(citations)
    citations.sort()

    # print(citations[-4])

    for i in range(1, length):
        if citations[-i] > i:
            answer = i

    return answer


# 끝에서 N번째 수가 N보다 큰가? 에 대한 질문

'''

0 1 3 3 5 6

1 2 2 3 3 4 4 4 5 6 7 9

'''