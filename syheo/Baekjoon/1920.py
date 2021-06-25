#solved.ac
#실버4
#이진탐색
#수 찾기
#1920

# N개의 정수 A[1], A[2], …, A[N]이 주어져 있을 때, 이 안에 X라는 정수가 존재하는지 알아내는 프로그램을 작성하시오.


#풀이 
#이진 탐색 

import sys
input = sys.stdin.readline

def binary_search(item):
    first = 0
    end = N-1 
    result = 0
    while first<=end:
        middle = (first+end)//2
        if NList[middle] < item:
            first = middle + 1
        elif NList[middle] > item:
            end = middle - 1 
        else:
            result = 1
            break
    return result 

N = int(input().rstrip())
NList = list(map(int,input().rstrip().split()))
NList.sort()
M = int(input().rstrip())
MList = list(map(int,input().rstrip().split()))

for m in MList:
    print(binary_search(m))



