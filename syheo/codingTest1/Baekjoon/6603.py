#solved.ac
#실버2
#조합
#로또
#6603
import sys
from itertools import combinations
input = sys.stdin.readline

while True: 
    sList = list(map(int,input().split()))
    if sList[0]==0:
        break
    for item in list(combinations(sList[1:],6)):
        print(*item)
    print()

