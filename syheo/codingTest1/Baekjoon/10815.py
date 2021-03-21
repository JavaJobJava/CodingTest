#solved.ac
#실버4
#정렬
#숫자카드
#10815

#상근이 숫자카드 N개
#정수 M개

#풀이 
#최대 크기만큼의 배열 생성 (2개 -> 하나는 양수, 음수 용)
#계수정렬을 이욯한 정렬 

import sys
input = sys.stdin.readline

MAX_SIZE = 10000000

#계수리스트 초기화 
plus = [0 for _ in range(MAX_SIZE+1)]
minus = [0 for _ in range(MAX_SIZE+1)]

#정답 리스트 
answer = []

N = int(input())
NList = list(map(int,input().split()))

#계수 리스트에 입력 
for n in NList:
    if n>=0:
        plus[n] += 1 
    elif n<0:
        minus[-n] +=1

M = int(input())
MList = list(map(int,input().split()))

for m in MList:
    if m>=0:
        if plus[m]==0:
            answer.append(0)
        else:
            answer.append(1)
    elif m<0:
        if minus[-m]==0:
            answer.append(0)
        else:
            answer.append(1)

for i in range(len(MList)):
    print(answer[i],end=' ')



