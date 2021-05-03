#CH11 그리디 기출
#예제 11-6
#무지의 먹방 라이브
#백준 18406
#브론즈 2

N = input()

left_sum = 0 
right_sum = 0
n_len = len(N)
for i in range(n_len//2):
    left_sum+=int(N[i])
for i in range(n_len//2,n_len):
    right_sum+=int(N[i])

if left_sum==right_sum:
    print("LUCKY")
else:
    print("READY")
