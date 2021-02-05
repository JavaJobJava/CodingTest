#CH4 구현
#예제 4-1
#상하좌우

# 이거 완전히 우리학교 코딩대회 형식 
# N 입력 받고 
# cmd(command) 문자열 입력 받음
# L : 행 1 , R : 행 N , U : 열 1 , D : 열 N 일 때 무시
# 아니면 이동

locX = 1
locY = 1
N = int(input())

cmd = input()
cmdList = cmd.split(" ")

for item in cmdList:
    if item=='L':
        if locY!=1:
            locY-=1

    if item=='R':
        if locY!=N:
            locY+=1
    
    if item=='U':
        if locX!=1:
            locX-=1
    
    if item=='D':
        if locX!=N:
            locX+=1
print(locX,locY,sep=" ",end="")
