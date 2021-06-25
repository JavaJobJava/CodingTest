#solved.ac
#실버3
#그리디
#ATM
#11399

#N명이 줄 서있음
#1-N 번호 ,i번 돈 인출 시간 Pi분

# 사람 수
N = int(input())

# 걸리는 시간 Pi
PList = list(map(int,input().split()))
sum = 0
for i in reversed(range(N)):
    sum +=  PList.pop(PList.index(min(PList)))*(i+1)
    
    # 뭐가 더 나을까 한줄 두줄 
    #sum += min(PList)*(i+1)
    #PList.pop(min(PList))

print(sum)