#solved.ac
#실버5
#이진 탐색
#수들의 합
#1789

# 서로다른 N 개의 자연수의 합이 S라고할때, S를 알떄, 자연수 N의 최댓값은?

def check(n):
    return n*(n+1)/2

s = int(input())

# n(n+1)/2 가 s보다 커지기 바로 직전 n 값 찾기 
# 이진 탐색으로 탐색 
bottom = 1
top = 4294967295
    
while True:
    #중간값 설정
    middle = (bottom+top)//2
    #바텀과 탑이 같아졌을 경우 check 값에 따라 결과 값 설정 
    if bottom == top:
        if check(middle)>s:
            middle = middle -1 
        break
    #비교 후 bottom or top 재 설정 
    if check(middle)<s: 
        bottom = middle+1
    elif check(middle)>s:
        top = middle-1
    #합과 같을 경우 탈출 
    else:
        break

print(middle)