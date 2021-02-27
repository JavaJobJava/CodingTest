#1003
#피보나치 함수  

def fibo(num,result):
    if num ==0:
        result[0]+=1
        return 0
    elif num == 1:
        result[1]+=1
        return 1
    else: return fibo(num-1,result)+fibo(num-2,result)

#테스트 케이스
T = int(input())
numList = []

for i in range(T):
    numList.append(int(input()))

for i in numList:
    result = [0,0]
    
    fibo(i,result)
    print(result[0],result[1],sep=" ")
