#프로그래머스 
#고득점 Kit
#dp
#level3
#N으로 표현

N =5
number = 12

def solution(N, number):
    answer = 0
    dp = [[number]*37 for _ in range(9)]
    
    if number == N: 
        return 1
    answer = 2 
    while answer<=8:
        for j in range(36):
            print(j,answer)
            if j//6==0:
                dp[answer][j]=dp[answer-1][j//6]+number
            elif j//6==1:
                dp[answer][j]=dp[answer-1][j//6]*number
            elif j//6==2:
                dp[answer][j]=dp[answer-1][j//6]-number
            elif j//6==3:
                dp[answer][j]=dp[answer-1][j//6]//number
            elif j//6==5:
                dp[answer][j]=dp[answer-1][j//6]+number*pow(10,len(str(number)))
            if dp[answer][j]==N:
                print('ad')
                return answer 
        answer +=1

    return answer

solution(N,number)