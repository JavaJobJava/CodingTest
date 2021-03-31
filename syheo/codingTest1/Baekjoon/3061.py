#solved.ac
#실버4
#그리디 
#사다리 타기
#3061
import sys 
input = sys.stdin.readline

cntList = []

#스왑 변형 병합 메서드 
def swap(array,x,cur,N):
    if cur<x:
        array = array[0:cur] + array[cur+1:x+1] + array[cur:cur+1]+ array[x+1:N+1]
    else: 
        array = array[0:x] + array[cur:cur+1] + array[x:cur]+array[cur+1:N+1]
    return array

for i in range(int(input())):
    N = int(input())
    #도착점이 index , 시작점이 value 
    arr = list(map(int,input().split()))
    arr.insert(0,0)
    #ladder = [0 for _ in range(N)] 
    #카운트 변수 
    cnt = 0
    #swapping 해서 1번~N번까지 위치를 찾아주며 오름차순 정렬  
    for j in range(1,N+1):
        #cur이 j의 위치로 가야 되는 index 값 0  1  6  2 3  4 5 7 
        cur = arr.index(j)
        if cur!=j:
            cnt+=abs(cur-j)
            arr =swap(arr,j,cur,N)
            #print(arr)
    cntList.append(cnt)
    #print(arr)

for i in cntList:
    print(i)

