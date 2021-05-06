score = [0] * 5
score = list(map(float, input().split()))
tempscore = score
# print(score)
sorted_score = sorted(score, reverse=True)#score.sort(reverse=True)
sorted_score_list = [0] * 5
visited = [0] * 5

for i in range(5):
    for j in range(5):
        if sorted_score[i] == tempscore[j]:
            sorted_score_list[i] = chr(j+65)
            tempscore[j] += 9999
            break


n, m = map(int, input().split())
watch = [[]*m for _ in range(n)]
genre = [[]*m for _ in range(n)]

Y = [[0, 0] for _ in range(n*m)]
O = [[0, 0] for _ in range(n*m)]
W = [[0, 0] for _ in range(n*m)]
ycount = 0
ocount = 0
wcount = 0

yprefer = [0] * (n*m)
oprefer = [0] * (n*m)


for i in range(n):
    watch[i] = list(input())

for i in range(n):
    genre[i] = list(input())

for i in range(n):
    for j in range(m):
        if watch[i][j] == 'Y':
            Y[ycount] = [i, j]
            ycount += 1
        elif watch[i][j] == 'O':
            O[ocount] = [i, j]
            ocount += 1
        elif watch[i][j] == 'W':
            W[wcount] = [i, j]
            wcount += 1




for j in range(5):
    for i in range(ycount):
        if genre[Y[i][0]][Y[i][1]] == sorted_score_list[j]:
            yprefer[i] = sorted_score[j]
for j in range(5):
    for i in range(ocount):
        if genre[O[i][0]][O[i][1]] == sorted_score_list[j]:
            oprefer[i] = sorted_score[j]

for j in range(5):
    for i in range(ycount):
        if sorted_score[j] == yprefer[i]:
            print(genre[Y[i][0]][Y[i][1]], sorted_score[j], Y[i][0], Y[i][1])
            yprefer[i] += 9999

for j in range(5):
    for i in range(ocount):
        if sorted_score[j] == oprefer[i]:
            print(genre[O[i][0]][O[i][1]], sorted_score[j], O[i][0], O[i][1])
            oprefer[i] += 9999

