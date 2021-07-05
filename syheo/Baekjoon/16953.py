#solved.ac
#실버1
#그리디
#A->B
#16953

# 연산 2가지
# 2를 곱함
# 1을 수의 가장 오른쪽에 추가함.
# A->B 로 바꾸는데 필요한 연산의 최솟값을 구해보자.

# A*2, A*10+1

def twodivide(num):
    return num//2

def tenone(num):
    return (num-1)//10

A,B = map(int,input().split())

cnt = 1

while B>A:
    cnt+=1
    #B의 1의 자리수 
    oneNum = B%10
    if oneNum==1:
        B=tenone(B)
    elif oneNum%2==0:
        B=twodivide(B)
    else:
        break


#결과 출력 
if A!=B:
    print(-1)
else:
    print(cnt)




