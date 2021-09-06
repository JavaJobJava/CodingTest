
from itertools import combinations
from string import ascii_lowercase

antatica = ['a', 'c', 'i', 'n', 't']

def brute_force(alpha, cnt):
    if cnt == k:
        temp = 0
        for i in range(n):
            flag = 0
            for j in range(len(check[i])):
                if not alphabet[]

n, k = map(int, input().split())
if k < 5:
    print(0)
    return

arr = [list(map(str, input())) for _ in range(n)]
alphabet = [False] * 26
for i in range(5):
    alphabet[ord(antatica[i]) - ord('a')] = True
print(alphabet)
#teach = list(combinations(list(ascii_lowercase), k - 5))
word = []
for i in range(n):
    word.append(arr[i][4:-4])

for i in range(n):
    check = []

    for j in range(len(word[i])):
        if word[i][j] not in antatica:
            check.append(word[i][j])
    check = set(check)

brute_force(0, 0)
    #for i in range(len(check)):
