#solved.ac
#골드3
#그리디
#저울
#2437
import sys 
input = sys.stdin.readline

#아이디어 
#ans ==> 현재까지 측정 가능한 물건의 최대 무게 
#ans + 1 ==> 현재로 측정할 수 없는 최소 무게 
#ans + chu ==> 만약 ans가 chu보다 크거나 같으면 ans 를 현재 추의 무게까지 더하여 갱신.

N = int(input())
ans = 1
chuList = list(map(int,input().split()))
chuList.sort()
for chu in chuList:
    if ans<chu:
        break
    ans+=chu
print(ans)

