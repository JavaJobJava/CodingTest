# 무적권 재귀문제, 소인수분해
def factorization(x):
    d = 2
    result = []
    while d <= x:
        if x % d == 0:
            result.append(d)
            x = x / d
        else:
            d = d + 1
    return result


def recur(arr, divide):
    result = []
    length = len(arr)  # 부분배열의 갯수



    print('arr = ', arr)
    #print('length = ', length)
    for i in range(length):
        node = [[] for _ in range(divide)]
        for j in range(len(arr[i])):
            index = j % divide
            node[index].append(arr[i][j])

        for k in range(divide):
            result.append(node[k])


    print('result = ', result)
    return result


def solution(n):
    answer = []
    p = []  # 소인수분해 결과
    p = factorization(n)
    arr = list(range(1, n + 1))
    for i in range(len(p)):
        if i == 0:
            arr = recur([arr], p[i])
        else:
            arr = recur(arr, p[i])
    for i in range(n):
        answer.append(arr[i][0])

    return answer