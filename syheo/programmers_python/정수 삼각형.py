#프로그래머스 
#고득점 Kit
#동적 계획법
#level3
#정수 삼각형

def solution(triangle):
    answer = 0
    length = len(triangle)
    dp = [[0]*i for i in range(1,length+1)]
    # 꼭대기 값 넣어줌
    dp[0][0]=triangle[0][0]
    #마지막-1줄까지 갈 수 있는 경로에 dp값을 갱신시킴
    for i in range(length-1):
        for j in range(i+1):
            dp[i+1][j]=max(triangle[i+1][j]+dp[i][j],dp[i+1][j])
            dp[i+1][j+1]=max(triangle[i+1][j+1]+dp[i][j],dp[i+1][j+1])
                        
    answer = max(dp[length-1])
    return answer 