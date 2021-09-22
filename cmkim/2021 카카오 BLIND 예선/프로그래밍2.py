import string
import math
tmp = string.digits


def convert(num, base):
    if base == 10:
        return num
    q, r = divmod(num, base)
    if q == 0:
        return tmp[r]
    else:
        return convert(q, base) + tmp[r]


def is_prime(x):
    if x == 1:
        return False
    for i in range(2, int(math.sqrt(x))+1):
        if x % i == 0:
            return False

    return True


def compress(x):
    result = ''
    flag = 0
    right = 0
    # print(type(x))
    for i in range(len(x) - 1, -1, -1):
        # print('i = ',i)
        if x[i] == '0':
            right += 1
        else:
            break
    # print('right = ', right)
    if right:
        x = x[0:-(right)]
    # print('x = ',x)
    for i in range(len(x)):
        if x[i] != '0':
            result += x[i]
            flag = 0
        elif flag == 0:
            result += '0'
            flag = 1
        elif flag == 1:
            continue
    # print(result)
    return result


def solution(n, k):
    answer = -1
    num = convert(n, k)
    # print(num)
    arr = compress(str(num))  # 0압축하기, 오른쪽 0 제거
    # print(arr)
    # print(type(arr))
    arr = arr.split('0')  # 0제거한 수
    prime = []
    print(arr)
    for i in range(len(arr)):  # 0제거한 수에서 소수뽑아내기
        # print(int(arr[i]))
        if is_prime(int(arr[i])):
            prime.append(int(arr[i]))
    # print(prime)

    answer = len(prime)

    return answer
