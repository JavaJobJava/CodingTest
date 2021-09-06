#CH11 그리디 기출
#예제 11-3
#문자열 뒤집기

#solved.ac
#실버5
#그리디
#문자열 뒤집기
#1439

import sys 
input = sys.stdin.readline
string = input().rstrip()
cnt0=0
cnt1=0

cur = -1
for s in string:
    s =int(s)
    if s!=cur:
        if s==0:
            cnt0+=1
        else:
            cnt1+=1
        cur=s
print(min(cnt0,cnt1))