from collections import deque
import math
N, number = 57, 400

def solution(N, number):
    answer = 1
    q = deque([(number,1)])
    while q:
        #print(q)
        num, cnt = q.popleft()
        if cnt > 8:
            answer = -1
            break
        if num == N:
            answer = cnt 
            break
        #5가지 연산 수행 
        print(int('00'))
        q.append((num*N,cnt+1))
        
        q.append((num//N,cnt+1))
        q.append((num+N,cnt+1))
        q.append((num-N,cnt+1))
        print('info:',num,str(num)[-len(str(N)):],int(str(num)[0:-len(str(N))]),cnt+1)
        if num>=N and str(num)[-len(str(N)):]==str(N):
            
            q.append((int(str(num)[0:-len(str(N))]),cnt+1))
        
    
    return answer
solution(N,number)