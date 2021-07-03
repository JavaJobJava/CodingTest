"""
@file 전화번호목록.py
@brief 해시 - Level 2
@desc
트라이 구조 생각했는데 구현 빡셈

첫 문제 풀이 -> 효율성 테스트 모두 실패
두 번째 문제 풀이 -> 딕셔너리 자료구조 활용
+) 다른 사람 풀이 중 제일 간단한 것
"""

# v1 : O(N^2) / 효율성 테스트 실패
def solution1(phone_book):
    answer = True
    
    length = len(phone_book)
    for i in range(length):
        for j in range(length):
            if i != j:
                if phone_book[i].startswith(phone_book[j]):
                    answer = False
                    break
    
    return answer


# v2
def solution(phone_book):
    answer = True

    prefixes = dict()
    for pb in phone_book:
        for i in range(len(pb)):
            prefix = pb[0:i+1]
            if prefix in prefixes:
                prefixes[prefix] += 1
            else:
                prefixes[prefix] = 0

    for pb in phone_book:
        if prefixes[pb] >= 1:
            answer = False
            break

    return answer

# 다른 사람 풀이
def solution3(phoneBook):
    phoneBook = sorted(phoneBook)

    for p1, p2 in zip(phoneBook, phoneBook[1:]):
        if p2.startswith(p1):
            return False
    return True