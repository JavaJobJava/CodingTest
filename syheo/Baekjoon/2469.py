#solved.ac
#실버1
#?
#사다리 타기
#2469
# 10
# 5
# 첫번쨰 아이디어 
# ????줄의 경우의 수를 bfs로 모두 구한 뒤 입력받은 결과와 비교 -> 시간초과
# 두번쨰 아이디어
# ????줄 기준 위 아래 결과를 구하고(first_sort,second_sort), ????줄에 의해 둘이 같아질 수 있는지 검사.

import sys
input=sys.stdin.readline

#??????줄이 나오기 전까지 sort, 나오면 해당 줄 리턴
def first_sort(n,k):
    for i in range(n):
        for j in range(k-1):
            if ladders[i][j]=='?':
                return i
            elif ladders[i][j]=='-':
                first_persons[j],first_persons[j+1]=first_persons[j+1],first_persons[j]

def second_sort(n,questionIdx):
    for i in range(n-1,questionIdx,-1):
        for j in range(k-1):
            if ladders[i][j]=='-':
                persons[j],persons[j+1]=persons[j+1],persons[j]


#사람 수 , 가로줄 수, 사다리 결과 
k = int(input())
n = int(input())
persons = list(input())
#A~?(k 만큼 알파벳 솔팅)
first_persons = [chr(65+i) for i in range(k)]

ladders = []

for i in range(n):
    ladders.append(list(input()))

questionIdx = first_sort(n,k)
second_sort(n,questionIdx)

isNoCase = False 
res = ''
#정답 가능 줄 만들기 
for i in range(k-1):
    if first_persons[i]==persons[i]:
        res += '*'
    elif first_persons[i] == persons[i+1]:
        res += '-'
    elif i !=0 and first_persons[i] == persons[i-1] and res[i-1]=='-':
        res += '*'
    else:
        isNoCase=True
        break

if isNoCase:
    for i in range(k-1):
        print('x',end='')
else:
    print(res)
