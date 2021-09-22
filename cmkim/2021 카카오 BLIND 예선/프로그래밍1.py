def solution(id_list, report, k):
    answer = []
    size = len(id_list)
    arr = [[0] * size for _ in range(size)]
    result = []
    dic = {string: i for i, string in enumerate(id_list)}
    #print(dic)

    for i in range(len(report)):
        str = report[i].split()
        a, b = str[0], str[1]
        # print(a, b)
        arr[dic[a]][dic[b]] += 1  # a가 b를 신고한것

    # for i in range(size):
    #     print(arr[i])

    for i in range(size):
        sum = 0
        for j in range(size):
            if arr[j][i]:
                sum += 1

        if sum >= k:
            result.append(1)
        else:
            result.append(0)

    # print('result = ',result)

    for i in range(size):
        sum = 0
        for j in range(size):
            if arr[i][j] and result[j]:
                sum += 1
        answer.append(sum)

    return answer
