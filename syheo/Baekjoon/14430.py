#solved.ac
#실버2
#dp
#자원 캐기
#14430

# (1,1)-(N,M)
# 오른쪽, 아래쪽 하나만 이동 가능 

#행 , 열 입력 
N,M = map(int,input().split())
#지도 
maps = []

#지도 입력
for i in range(N):
    tmp = list(map(int,input().split()))
    maps.append(tmp)

#dp 테이블 입력 
dp = [[0]*(M+1) for _ in range(N+1)]
#maxV= 0
for i in range(1,N+1):
    for j in range(1,M+1):
        #이전 것중 큰거 넣기 
        dp[i][j]=max(dp[i-1][j],dp[i][j-1])
        #해당 칸에 자원이 있을 경우 1플러스 
        if maps[i-1][j-1]==1:
            dp[i][j]+=1
        #maxV = max(maxV,dp[i][j])

print(dp[N][M])