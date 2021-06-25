import re

N = int(input())
indexList = []
for i in range(N):
    indexList.append(input())
Q = int(input())

for i in range(Q):
    tmp = input()
    cnt = 0
    r = re.compile('.(%s).'%tmp)
    tmpList = list(filter(r.match, indexList)) 
    print(tmpList)
    for j in indexList:
        match = re.findall(re.escape(tmp), j)
        #print('match',match)
        cnt+=len(match)
    #print(cnt)

