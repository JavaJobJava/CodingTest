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
#cnt 변수를 하나만 두고 2로 나눈 몫을 출력해도 됨.
#0->1 으로 바뀌는 횟수와 1->0으로 바뀌는 횟수는 최대 1번 밖에 차이가 나지 않기 때문임.

