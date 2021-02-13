#solved.ac
#실버1
#그리디
#신입사원
#1946

#어떤 회사의 채용 규칙 : 서류와 면접 두 점수 중 하나라도 다른 지원자보다 점수가 높아야 채용이 가능함.

# 첫째줄 테스트 케이스 갯수 T
# 테스트 케이스의 사람 수 N
# 서류 등수 및 면접 등수 rankd, ranki

#풀이 노트
## 1번째 시도 
# 튜플로 구성된 rank 리스트로 받기
# 서류 면접 등수로 정렬 
# 지원자 중 한 명은 자기보다 높은 랭크의 사람보다 다른 하나의 등수가 높으면 채용 
## 2번째 시도
# 높은 순위부터 검사를 하다 보면 뒤에 검사를 안해도 될때가 오지 않을까 
# 서류 1등 면접1등 서류2등 면접2등 서류3등 면접3등 ...
## 3번째 시도 
# 규칙-> 두 점수가 모두 다른 지원자보다 낮으면 탈락 
# max 값으로 설정 후 비교 
# 입력 받을 때마다 검사 후 맥스값 설정 
## 4번째 시도 
# 정렬 후 랭크 max 값 설정으로 비교 


from operator import itemgetter
import sys

#입력값 받기 
T = int(input())
# 채용 최대 인원 
cnt = [0 for _ in range(T)]

for i in range(T):
    # 채용 최대 인원 
    #cnt = 0
    maxd = 100001
    maxi = 100001
    N = int(input())
    rank=[]
    #rank = [() for _ in range(N)]
    for j in range(N):
        rank.append(tuple(map(int, sys.stdin.readline().split())))
        #swap 
        if j>0:
            if rank[j][0] < rank[j-1][0]:
                rank[j],rank[j-1] = rank[j-1], rank[j]
    print(rank)
    for x,y in rank:
        if y<maxi:
            cnt[i]+=1
            maxi=y
        if maxi==1:
            break
for cntitem in cnt:
    print(cntitem)


