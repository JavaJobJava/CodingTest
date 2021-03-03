#solved.ac
#실버4
#정렬
#숫자카드
#10815

#상근이 숫자카드 N개
#정수 M개

#풀이 
#이진 탐색 

import sys
input = sys.stdin.readline

def binary_search(NList,item):
    first = 0 
    end = len(NList)-1
    result = 0
    while True:
        middle = (first+end)//2
        #종료조건
        if first>end:
            break
        if NList[middle]>item:
            end = middle - 1
        elif NList[middle]<item:
            first = middle + 1
        else:
            result = 1
            break
    return result 

#정답 리스트 
answer = []

N = int(input())
NList = list(map(int,input().split()))
NList.sort()

M = int(input())
MList = list(map(int,input().split()))

for m in MList:
    answer.append(binary_search(NList,m))

for i in range(len(MList)):
    print(answer[i],end=' ')