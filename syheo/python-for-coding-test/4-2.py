#CH4 구현
#예제 4-2
#시각

# 00분 00초 ~ 59분 59초 반복 횟수 N+1
# 3시 13시 23시 예외 
# 경우의 수 (N+1) * 60 * 60

N = int(input())
cnt = 0

hour = 0 
min = 0 
sec = 0

for h in range(0,N+1):
    for m in range(0,60):
        for s in range(0,60):
            if str(h).find('3')!=-1 or str(m).find('3')!=-1 or str(s).find('3')!=-1: 
                cnt+=1

print(cnt)
            



