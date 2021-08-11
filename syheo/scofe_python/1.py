
#3
#12:00 ~ 23:59
#11:00 ~ 18:00
#14:00 ~ 20:00



N = int(input())
timeList = [[0]*4 for _ in range(N)]

startH = -1
endH = 24
startM = -1
endM = 60

for i in range(N):
    tmp = input()
    timeList[i][0]= int(tmp[0:2])
    timeList[i][1]= int(tmp[3:5])
    timeList[i][2]= int(tmp[8:10])
    timeList[i][3]= int(tmp[11:13])
    if startH < timeList[i][0]:
        startH=timeList[i][0]
        startM = timeList[i][1]
    elif startH == timeList[i][0]:
        startH=timeList[i][0]
        startM = max(startM,timeList[i][1])
    if endH > timeList[i][2]:
        endH = timeList[i][2]
        endM = timeList[i][3]
    elif endH == timeList[i][2]:
        endH = timeList[i][2]
        endM = min(endM,timeList[i][3])
#print(timeList)
if startH>endH:
	print(-1)
elif (startH==endH and startM>endM):
	print(-1)
else: 
	print("%02d:%02d ~ %02d:%02d"%(startH,startM,endH,endM))

