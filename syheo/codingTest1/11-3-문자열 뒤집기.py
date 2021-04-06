#CH11 그리디 기출
#예제 11-3
#문자열 뒤집기
import sys 
input = sys.stdin.readline
string = input().rstrip()
cnt=[0,0]

cur = -1
for s in string:
    s =int(s)
    if s!=cur:
        cnt[s]+=1
        cur=s
print(min(cnt[0],cnt[1]))
