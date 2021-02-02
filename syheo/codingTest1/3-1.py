#CH3 그리디
#예제 3-1
#거스름돈

N = int(input())
coin=[500, 100, 50, 10]
cnt = 0 # 동전의 갯수 
for i in coin:
    cnt += N//i
    N=N%i

print(cnt)
