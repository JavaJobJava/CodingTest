#solved.ac
#실버5
#구현
#Base Conversion
#11576



A,B = map(int,input().split())
m = int(input())

numList = list(map(int,input().split()))

sum = 0
numList.reverse()

for num in range(m):
    sum+=(A**num)*numList[num]

answer = []
while sum//B!=0:
    answer.append(sum%B)
    sum//=B
answer.append(sum%B)

answer.reverse()
for a in answer:
    print(a,end=" ")


    
