#solved.ac
#실버1
#이분탐색
#케이크 자르기
#17179

import sys 
input = sys.stdin.readline

N,M,L = map(int,input().split())

cuts = []
cnts = []

#자를 수 있는 지점 입력
for i in range(M):
    cuts.append(int(input()))

cuts = [0]+cuts+[L]

#자르는 횟수의 목록 입력 
for i in range(N):
    cnts.append(int(input()))

def calculate(mid,cnt):
    prev = 0 
    #mid보다 크거나 같은 조각으로 자르기 
    for i in range(1,len(cuts)):
        sum = cuts[i]-cuts[prev]
        if sum >= mid:
            cnt-=1
            prev = i
        if cnt == 0:
            break
    #cnt는 자르는데 남은 횟수, 마지막 sum이 mid보다 크거나 같은지 확인해야 함. -> 정답이 될 수 있는 길이 
    if (cnt == 0 and cuts[-1]-cuts[prev]>=mid):
        return True
    #정답이 될 수 없는 길이 
    return False

for cnt in cnts:
    answer = 0
    left = 0
    right = L 
    while left <= right: 
        mid = (left+right)//2
        if calculate(mid,cnt):
            left = mid+1
            answer=max(answer,mid)
        else:
            right = mid-1
    print(answer)

