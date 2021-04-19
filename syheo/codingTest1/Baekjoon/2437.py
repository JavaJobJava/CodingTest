#solved.ac
#골드3
#그리디
#저울
#2437
import sys 
input = sys.stdin.readline

N = int(input())
ans = 1
chuList = list(map(int,input().split()))
chuList.sort()
for chu in chuList:
    if ans<chu:
        break
    ans+=chu
print(ans)

