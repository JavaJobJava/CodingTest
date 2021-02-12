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
## 4번째 시도 
# 정렬 후 랭크 max 값 설정으로 비교 


from operator import itemgetter

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
    rank = [() for _ in range(N)]
    for j in range(N):
        rank[j] = tuple(map(int,input().split()))
        # # 검사
        # if maxd>rank[j][0]: 
        #     maxd=rank[j][0]
        # elif maxi>rank[j][1]:
        #     maxi=rank[j][1]
        
        # else:
        #     pass
    #print(maxd,maxi)
    
    document = sorted(rank,key=itemgetter(0))
    for x,y in document:
        if y<maxi:
            cnt[i]+=1
            maxi=y
        if maxi==1:
            break
    #interview = sorted(rank,key=itemgetter(1))
    #print(document)
    #print(interview)
for cntitem in cnt:
    print(cntitem)


    # # 다차원 배열 정렬 방법 sort(reverse=?, key=itemgetter(index,) 
    # rank.sort(key=itemgetter(0),reverse=False)
    # # 검사 
    # for k in range(1,N):
    #     check = 1
    #     for j in range(k):
    #         if rank[j][1]<rank[k][1]:
    #             check = 0
    #     if check==1:
    #         cnt[i] +=1

# for c in cnt:
#     print(c,end=" ")



