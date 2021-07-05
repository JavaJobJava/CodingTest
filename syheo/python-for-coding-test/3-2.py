#CH3 그리디
#예제 3-2
#큰 수의 법칙

N = int(input()) #배열의 크기
M = int(input()) #숫자가 더해지는 횟수
K = int(input()) #연속 제한 횟수 
array = []
sum = 0
flag = 0
for i in range(N):
    tmp = int(input())
    array.append(tmp)
array.sort()

for i in range(M):
    if flag<K:
        print(array[N-1])
        sum+=array[N-1]
        flag+=1
    else:
        print(array[N-2])
        sum+=array[N-2]
        flag=0

print(sum)

