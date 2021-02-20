# X지원자의 상위호환이 있는지? 찾는문제.
# 리스트 형태로 데이터 저장 or 다른 자료형?
# 나보다 못하는 사람을 찾는게 아닌, 나보다 잘하는 사람이 나머지 과목마저 잘하는가?
import sys

T = int(input())

a=[]
b=[]
for i in range(T): #테스트 케이스마다
    N = int(input()) #지원자수 입력

    count = N
    for index in range(N): #지원자 점수 입력
        A, B = map(int, sys.stdin.readline().split())

        a.append(A)
        b.append(B)



    for j in range(N):
        for k in range(N):
            if a[j]>a[k] and b[j]>b[k] : #나보다 더 잘한놈이 있으면
                count -= 1
                break
            else:
                continue

    a.clear()
    b.clear()
    print(count)

#arr=[]
    #     arr.append((A,B))
    # for a in arr:
    #     for b in arr:
    #         if a[0]>b[0] and a[1]>b[1] :
    #             count -= 1
    #             break;

    #arr.clear()
