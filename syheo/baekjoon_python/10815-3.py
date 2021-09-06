#solved.ac
#실버4
#정렬
#숫자카드
#10815

#상근이 숫자카드 N개
#정수 M개

#풀이 
#set 자료형을 이용하여 탐색 

import sys
input = sys.stdin.readline

N = int(input())
NSet = set(list(map(int,input().rstrip().split())))

M = int(input())
MList = list(map(int,input().rstrip().split()))

for m in MList:
    if m in NSet:
        print(1,end=' ')
    else:
        print(0,end=' ')

