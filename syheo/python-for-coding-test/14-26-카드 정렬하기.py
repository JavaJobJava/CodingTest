#CH14 정렬기출
#예제 14-26
#카드 정렬하기
#백준 1715
#골드 4

# 아이디어 
# 우선순위 큐를 사용하여 최소값 둘을 뽑아 합한뒤 heappush하여 연산함.

import heapq
import sys 
input = sys.stdin.readline

N = int(input())

answer = 0

cards = [int(input()) for i in range(N)]

heapq.heapify(cards)

while True:
    if len(cards)==1:
        break
    rst = heapq.heappop(cards)+heapq.heappop(cards)
    heapq.heappush(cards, rst)
    answer += rst

print(answer)

