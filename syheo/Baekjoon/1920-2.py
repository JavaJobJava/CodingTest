#이진탐색
#수 찾기
#1920

# N개의 정수 A[1], A[2], …, A[N]이 주어져 있을 때, 이 안에 X라는 정수가 존재하는지 알아내는 프로그램을 작성하시오.


#풀이 
#set 자료형 
import sys
input = sys.stdin.readline


N = int(input().rstrip())
NSet = set(list(map(int,input().rstrip().split())))
M = int(input().rstrip())
MList = list(map(int,input().rstrip().split()))

for m in MList:
    if m in NSet:
        print(1)
    else:
        print(0)