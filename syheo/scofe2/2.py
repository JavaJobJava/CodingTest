import sys 
sys.setrecursionlimit(10**7)
input = sys.stdin.readline

N = int(input())

def find_path(last,visited):
    if visited == (1<<n)-1:  
        return info[country[last]][0] or INF  
    if DP[last][visited] is not None:  
        return DP[last][visited] 
    tmp=INF
    for city in range(n):
        if visited & (1 << city) == 0 and info[country[last]][city] != 0:
            tmp=min(tmp,find_path(city,visited|(1<<city)) + info[country[last]][city])
    DP[last][visited]=tmp
    return tmp

country = []
info = dict()
INF = int(10000)

for i in range(N): 
    c1, c2,cost = map(str,input().split())
    if c1 not in info.keys():
        country.append(c1)
        info[c1]=[0 for _ in range(6)]
    if c2 not in info.keys():
        country.append(c2)
        info[c2]=[0 for _ in range(6)]
    info[c1][country.index(c2)]=int(cost)
    info[c2][country.index(c1)]=int(cost)
n = len(country)

DP=[[None]*(1<<n) for _ in range(n)]


print(find_path(0,1<<0))



    

