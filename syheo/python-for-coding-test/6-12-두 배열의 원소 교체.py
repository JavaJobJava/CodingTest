#CH6 정렬
#예제 6-12
#두 배열의 원소 교체

# 동빈이는 두 개의 배열 A와 B를 갖고 잇음.
# 두 배열은 N개의 원소로 구성되어 있으며
# 배열의 원소는 모두 자연수.
# 최대 K번 바꿔치기 연산을 수행
# 바꿔치기 연산은 A에 있는 원소 하나와 배열 B 에 있는 원소 하나를 골라서 두 원소를 서로 바꾸는 것
# 동빈이의 최종 목표는 배열 A의 모든 원소의 합이 최대가 되도록 하는 것.

N,K = map(int,input().split())

sum = 0

A = list(map(int,input().split()))
B = list(map(int,input().split()))

#정렬
A.sort()
B.sort()

#교체
for i in range(K):
    if A[i]<B[N-i-1]:
        A[i],B[N-i-1] = B[N-i-1],A[i]
    else:
        break

for i in A:
    sum+=i

print(sum)