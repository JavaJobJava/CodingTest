#CH14 정렬기출
#예제 14-23
#국영수
#백준 10825
#실버 4

# 정렬조건
# 국어 점수가 감소하는 순서로
# 국어 점수가 같으면 영어 점수가 증가하는 순서로
# 국어 점수와 영어 점수가 같으면 수학 점수가 감소하는 순서로
# 모든 점수가 같으면 이름이 사전 순으로 증가하는 순서로

import sys 
input = sys.stdin.readline

N = int(input())

info = []

for i in range(N):
    info.append(tuple(map(str,input().rstrip().split())))

info.sort(key = lambda x: (-int(x[1]),int(x[2]),-int(x[3]),(x[0])))

for i in range(N):
    print(info[i][0])

