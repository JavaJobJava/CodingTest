#solved.ac
#실버2
#dp
#안녕
#1535

#풀이 
#dp 테이블 만들어서 
#체력은 100, 체력이 0이 될때 까지 

N = int(input())

#행은 사람 수 , 열은 최대 체력 
dp = [[0]*100 for _ in range(N+1)]

# 체력 
L = list(map(int,input().split()))
# 기쁨 
J = list(map(int,input().split()))

maxJoy = 0

#사람의 수만큼 반복
for i in range(0,N):
    # 1체력 있을 경우 부터 최대 체력 99까지 
    for j in range(1,100):
        # i번사람 소모 체력과 j(체력) 비교 
        if L[i]<=j : 
            #j체력일 경우 i번사람 : i번사람기쁨+(현재 체력-i번사람 소모 체력)의 최대 기쁨 더한 것과, 안넣었을 경우를 비교하여 최댓값 넣음
            if i>=1:
                dp[i][j] = max(J[i] + dp[i-1][j - L[i]], dp[i-1][j])
            else: 
                dp[i][j] = J[i]
        else:
            #이전 행 같은 무게일 경우를 대입
            if i>=1:
                dp[i][j] = dp[i-1][j]
        #맥스값 계속 최신화 
        maxJoy = max(dp[i][j], maxJoy)

print(maxJoy)
