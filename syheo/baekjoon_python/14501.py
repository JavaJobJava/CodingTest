#solved.ac
#실버4
#DP
#퇴사
#14501

#일 하는 날 
N = int(input())

#시간, 보상 리스트 
T=[]
P=[]

#Ti , Pi 입력
for i in range(N):
    t,p = map(int,input().split())
    T.append(t)
    P.append(p)

#dp테이블 초기화 
dp = [0 for _ in range(N+1)]
maxP = 0 

#순차적으로
for i in range(N):
    if i+T[i]<=N:
        for j in range(i+T[i],N+1):
            dp[j] = max(dp[j],dp[i]+P[i])
            maxP = max(maxP,dp[j])

print(maxP)








