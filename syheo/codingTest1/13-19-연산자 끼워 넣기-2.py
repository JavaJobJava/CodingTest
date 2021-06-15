#CH13 BFSDFS기출
#예제 13-19
#연산자 끼워 넣기
#백준 14888
#실버 1

#덧셈, 뺼셈, 곱셈, 나눗셈

#아이디어 1
#1. 연산자 경우의 수를 모두 구함 -> bfs 
#2. 연산자 리스트가 완성되면 max, min 값에 값을 계산하면서 답을 구함.

#아이디어 2
#1. 계산 결과와 남은 연산자의 갯수를 저장-> bfs 
#2. 남은 연산자의 갯수가 없으면 계산 결과로 min, max return 

from collections import deque

def cal(a,b,cmd):
    if cmd == 0:
        return a+b
    elif cmd == 1:
        return a-b
    elif cmd == 2:
        return a*b
    elif cmd == 3:
        if a<0 or b<0:
            return -(abs(a)//abs(b))
        return a//b

N = int(input())

nums = list(map(int,input().split()))

cmdCnts = list(map(int,input().split()))

minValue = int(1e9)
maxValue = -int(1e9)

def bfs():
    global minValue, maxValue
    a,b,c,d = cmdCnts
    q = deque([(nums[0],1,a,b,c,d)])
    while q:
        rst, idx, a, b, c, d = q.popleft()
        #완성된 연산자 리스트 계산 후 max,min 값 비교
        if a+b+c+d == 0:
            minValue = min(rst,minValue)
            maxValue = max(rst,maxValue)  
        #연산자 경우의 수 모두 구하기 
        if a!=0:
            q.append((cal(rst,nums[idx],0),idx+1,a-1,b,c,d))
        if b!=0:
            q.append((cal(rst,nums[idx],1),idx+1,a,b-1,c,d))
        if c!=0:
            q.append((cal(rst,nums[idx],2),idx+1,a,b,c-1,d))
        if d!=0:
            q.append((cal(rst,nums[idx],3),idx+1,a,b,c,d-1))
            

bfs()
print(maxValue)
print(minValue)


