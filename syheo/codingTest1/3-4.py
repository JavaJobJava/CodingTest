#CH3 그리디
#예제 3-4
#1이 될  때까지

N, K = map(int,input().split()) #N이 1이 되는 ㅜ, K는 나누는 수 
cnt = 0 # 실행 횟수
while N!=1:
    if N%K==0:
        N//=K
    else:
        N-=1
    cnt+=1

print(cnt,end='')


