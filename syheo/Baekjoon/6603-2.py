#solved.ac
#실버2
#DFS 
#로또
#6603
import sys
input = sys.stdin.readline

def dfs(num,sLen,cnt,result,sList): 
    #예외처리
    if num >sLen:
        pass  
    else:
        result[cnt]=num
        #6개를 뽑았을 경우 
        if cnt==6: 
            #출력 
            for i in result[1:]:
                print(sList[i],end=' ')
            print()
        else:
            #s집합 원소 갯수에 따라 최대 이동 범위 설정 후 반복
            for i in range(1,sLen-4):
                dfs(num+i,sLen,cnt+1,result,sList)
            
while True: 
    sList = list(map(int,input().split()))
    if sList[0]==0:
        break
    sLen = sList[0]
    answer = [0 for i in range(7)]
    dfs(0,sLen,0,answer,sList)
    
    print()
