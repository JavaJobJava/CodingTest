n = int(input())

arr = [[]*15 for _ in range(n)]

min = '24:60'
max = '00:00'
for i in range(n):
    arr[i] = input()

maxtime = int(max[:2])
maxmin = int(max[3:5])
mintime = int(min[:2])
minmin = int(min[3:5])

starttime = '00:00'
endtime = '00:00'

for i in range(n):

    stime = int(arr[i][:2])
    smin = int(arr[i][3:5])
    etime = int(arr[i][8:10])
    emin = int(arr[i][11:13])

    if maxtime < stime:            #시작 시간중 가장 큰, 늦은 시간 구하기
        maxtime = stime
        maxmin = smin

    elif maxtime == stime and maxmin < smin:
        maxmin = smin

    if mintime > etime:             #종료 시간중 가장 작은, 빠른 시간 구하기
        mintime = etime
        minmin = emin

    elif mintime == etime and minmin > emin:
        minmin = emin


ttime1 = maxtime // 10
ttime2 = maxtime % 10
tmin1 = maxmin // 10
tmin2 = maxmin % 10

starttime = str(ttime1) + str(ttime2) + starttime[2:]
starttime = starttime[:3] + str(tmin1) + str(tmin2)

ttime1 = mintime // 10
ttime2 = mintime % 10
tmin1 = minmin // 10
tmin2 = minmin % 10

endtime = str(ttime1) + str(ttime2) + endtime[2:]
endtime = endtime[:3] + str(tmin1) + str(tmin2)


if maxtime < mintime:
    print(starttime, '~', endtime)
elif maxtime == mintime and maxmin <= minmin:
    print(starttime, '~', endtime)
else:
    print(-1)