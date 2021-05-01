#CH11 그리디 기출
#예제 11-4
#만들 수 없는 금액

N = int(input())
coins = list(map(int,input().split()))
answer = 1
coins.sort()
for i in range(N):
    if coins[i]<=answer:
        answer+=coins[i]
    else:
        print(answer)
    

