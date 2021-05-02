#CH11 그리디 기출
#예제 11-5
#볼링공 고르기

#N은 볼링공 갯수, M은 공의 최대 무게 
N , M = map(int,input().split())

balls = list(map(int,input().split()))
balls.sort()
sum = 0
postSum = 0
curSum = 0
cur = 0 
#현재 공 무게와 다른 이전 공의 갯수 * 현재 공 무게의 갯수를 sum에 더해나감
for ball in balls:
    if ball!=cur:
        cur = ball
        sum+=curSum*postSum
        postSum+=curSum
        curSum=1
    else:
        curSum+=1
sum+=curSum*postSum
print(sum)




