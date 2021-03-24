import sys
sys.setrecursionlimit(10**9)

N = int(input())
path = input()
cnt = 0 
def goPath(i):
    if i==N-1:
        return 1
    if i>=N: 
        return 0
    if int(path[i])==0:
        return 0

    else:
        cur1 = i+1
        cur2 = i+2
        return goPath(cur1)+goPath(cur2)

print(goPath(0))

