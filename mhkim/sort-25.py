"""
@file sort-25.py
@brief 카드 정렬하기
@desc 힙
"""
import sys
import heapq
input = sys.stdin.readline

n = int(input())

bundle = []
for i in range(n):
    heapq.heappush(bundle, int(input()))

cnt = 0
while len(bundle) > 1:
    first = heapq.heappop(bundle)
    second = heapq.heappop(bundle)
    cnt += first+second
    heapq.heappush(bundle, first + second)

print(cnt)
