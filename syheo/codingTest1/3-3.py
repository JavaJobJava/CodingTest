#CH3 그리디
#예제 3-3
#숫자 카드 게임 

N = int(input()) # 행의 개수
M = int(input()) # 열의 개수 
array = [[0] * M for i in range(N)]
sorted_first_index_list = []

for i in range(N):
    for j in range(M):
        array[i][j] = int(input())
    array[i].sort()
    sorted_first_index_list.append(array[i][0])

sorted_first_index_list.sort()

print(sorted_first_index_list[N-1], end='')