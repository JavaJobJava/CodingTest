"""
@file 소수찾기.py
@brief 완전탐색 - Level 2
@desc 
소수 판별 / 순열->리스트
"""

from itertools import permutations as pt
import math

def isPrime(n):
    if n < 2:
        return False

    for i in range(2, int(math.sqrt(n))+1):
        if n % i == 0:
            return False
    return True

def solution(numbers):
    nums = list(numbers)

    prime = set()
    for i in range(1, len(numbers)+1):
        p = list(pt(nums, i))
        p = list(map(''.join, p))
        for num in set(p):
            if isPrime(int(num)):
                prime.add(int(num))

    return len(prime)