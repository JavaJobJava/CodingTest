"""
@file 가장큰수.py
@brief 정렬 - Level 2
@desc 

"""
# 테스트 케이스 통과 / 시간 초과
from functools import cmp_to_key
from itertools import permutations as pt


def solution1(numbers):
    cases = list(pt(numbers, len(numbers)))

    l = []
    for c in cases:
        nums = list(map(str, c))
        num = ''.join(nums)
        l.append(num)

    l.sort()
    return l[-1]


# 앞자리가 큰 수 ->  앞자리 같을 경우 뒷자리순인데 자리수가 안맞으면 앞자리복사(3->33취급)  30 < 33 < 34 이렇게 비교하기 위해선?
# 수가 1000이하
def solution(numbers):
    # '0000' 예외처리
    # if max(numbers) == 0:
    #     return '0'
    nums = sorted(list(map(str, numbers)), key=lambda x: x*4, reverse=True)
    return str(int(''.join(nums)))  # int -> str : '0000'인 경우도 있기 때문에


# 다른 풀이 (comparator)
def comparator(a, b):
    t1 = a+b
    t2 = b+a
    # t1이 크다면 1  // t2가 크다면 -1  //  같으면 0
    return (int(t1) > int(t2)) - (int(t1) < int(t2))


def solution2(numbers):
    n = [str(x) for x in numbers]
    n = sorted(n, key=cmp_to_key(comparator), reverse=True)
    answer = str(int(''.join(n)))
    return answer
