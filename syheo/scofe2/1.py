
import sys
input = sys.stdin.readline

N, time = map(str,input().split())
N = int(N)
h = int(time[0:2])
m = int(time[3:5])
s = int(time[6:8])
times = h*60*60+ m*60 + s 

timeList = [0 for _ in range(N)]
dp= [0 for _ in range(N+1)]

maxSongIdx= -1
maxSong=-1
#플레이리스트 입력 
for i in range(N):
    tmp = input()
    timeList[i]=int(tmp[0:2])*60+int(tmp[3:5])

start = 0
sum = 0
cnt = 0
for i in range(N):
    sum+=timeList[i]
    cnt+=1
    if sum >=times:
        if maxSong<cnt:
            maxSong = cnt 
            maxSongIdx = start
        while sum>=times:
            sum-=timeList[start]
            start+=1
            cnt -= 1

        
print(maxSong,maxSongIdx+1,end=' ')  