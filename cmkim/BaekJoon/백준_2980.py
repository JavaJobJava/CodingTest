N, L = map(int, input().split())

arr =[]
tr = 0
n_tr = 0
time = 0
loc = 0
arr = [list(map(int, input().split())) for _ in range(N)]

def check(time, red, green):
    cycle = red + green
    time %= cycle
    if time >= red:
        return True
    elif time < red:
        return False


while loc < L :
    for i in range(N):
        tr = arr[i][0]          #신호등 위치 (현재 걸린 신호등)
        if i < N-1:               #다음 신호등 위치
            n_tr = arr[i+1][0]
        elif i == N-1:
             n_tr = L

        if loc < tr and loc == 0 :   #맨 처음 신호등까지 이동
            time += tr
            loc += tr

        dist = n_tr - tr        #다음 신호등 까지 이동해야 하는 거리
        while loc < n_tr :
            if check(time, arr[i][1], arr[i][2]) == True: #초록불
                time += dist
                loc += dist
            else:                                         #빨간불
                time += 1

print(time)