#1003
#피보나치 함수  

#dp 배열 초기화 
dzero= [0]*41
done = [0]*41
dp0 = [1,0]
dp1 = [0,1]
result = [0]*2

def fibozero(num):
    if num == 0: 
        return 1
    elif num == 1:
        return 0
    if dzero[num] != 0:
        return dzero[num]
    dzero[num] = fibozero(num-1) +fibozero(num-2)
    return dzero[num]

def fiboone(num):
    if num == 1: 
        return 1
    elif num == 0:
        return 0
    if done[num] != 0:
        return done[num]
    done[num] = fiboone(num-1) +fiboone(num-2)
    return done[num]

#미리 계산 
for i in range(2,41):
    dp0.append(dp0[i-1]+dp0[i-2])
    dp1.append(dp1[i-1]+dp1[i-2])

#테스트 케이스
T = int(input())
numList = []

for i in range(T):
    numList.append(int(input()))

for i in numList:    
    print(dp0[i],dp1[i],sep=" ")
    #print(fibozero(i),fiboone(i),sep=" ")

