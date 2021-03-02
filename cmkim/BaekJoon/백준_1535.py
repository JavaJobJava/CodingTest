import sys
input = sys.stdin.readline
n = int(input())
L = list(map(int, input().split())) #체력
J = list(map(int, input().split())) #기쁨
L, J = [0] + L, [0] + J     #1번 인덱스부터 사용하기 위해서 맨 앞에 땡겨준다
dp = [[0 for _ in range(101)] for _ in range(21)]


#print(L)
#print(J)
