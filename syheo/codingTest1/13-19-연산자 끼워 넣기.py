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

nums = deque(list(map(int,input().split())))

cmdCnts = list(map(int,input().split()))

def bfs():
    minValue = int(1e9)
    maxValue = -int(1e9)
    a,b,c,d = cmdCnts
    q = deque([([],a,b,c,d)])
    while q:
        cmdList, a, b, c, d = q.popleft()
        #완성된 연산자 리스트 계산 후 max,min 값 비교
        if a+b+c+d == 0:
            rst = nums[0]
            idx = 1
            for cmd in cmdList:
                rst = cal(rst,nums[idx],cmd)
                idx+=1
            minValue = min(rst,minValue)
            maxValue = max(rst,maxValue)  
        #연산자 경우의 수 모두 구하기 
        if a!=0:
            q.append((cmdList+[0],a-1,b,c,d))
        if b!=0:
            q.append((cmdList+[1],a,b-1,c,d))
        if c!=0:
            q.append((cmdList+[2],a,b,c-1,d))
        if d!=0:
            q.append((cmdList+[3],a,b,c,d-1))
            
    return (maxValue,minValue)

a,b = bfs()
print(a)
print(b)


