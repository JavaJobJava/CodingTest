#CH11 그리디 기출
#예제 11-1
#모험자 길드

N = int(input())
xList = list(map(int,input().split()))
xList.sort(reverse=True)
cnt = 0
#필요 인원수 
cur = xList[0]
for i in range(0,N):
    cur-=1
    if cur ==0:
        cnt+=1
        cur = xList[i]
print(cnt)