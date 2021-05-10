from collections import deque

def solution(places):
    answer = []

    for i in range(5):
        flag = 1
        p_list = []
        #p_ad_list = []
        q = deque()

        for x in range(5):
            for y in range(5):
                if places[i][x][y] == 'P':
                    p_list.append((x, y))

        for a in range(len(p_list)):
            for b in range(a+1, len(p_list)):
                if abs(p_list[a][0] - p_list[b][0]) + abs(p_list[a][1] - p_list[b][1]) < 3:
                    q.append((p_list[a][0], p_list[a][1], p_list[b][0], p_list[b][1]))
                    #p_ad_list.append((p_list[a][0], p_list[a][1], p_list[b][0], p_list[b][1]))
                    #print('adjacent', p_list[a][0], p_list[a][1], p_list[b][0], p_list[b][1])

#2칸 아래,
#2칸 우측
#1칸 좌측, 1칸 아래
#1칸 우측, 1칸 아래

        while q:
            x1, y1, x2, y2 = q.popleft()
            if x1 + 2 == x2:
                if places[i][x1 + 1][y1] == 'O':
                    flag -= 1
            elif y1 + 2 == y2:
                if places[i][x1][y1+1] == 'O':
                    flag -= 1
            elif y1 - 1 == y2 and x1 + 1 == x2: #왼쪽아래
                if places[i][x1][y2] == 'O' or places[i][x2][y1] == 'O':
                    flag -= 1
            elif y1 + 1 == y2 and x1 + 1 == x2:
                if places[i][x1][y2] == 'O' or places[i][x2][y1] == 'O':
                    flag -= 1
            elif x1 + 1 == x2 or y1 + 1 == y2:
                flag -= 1


        if flag > 0:
            answer.append(1)
        else:
            answer.append(0)

    return answer

print(solution([["POOOP", "OXXOX", "OPXPX", "OOXOX", "POXXP"], ["POOPX", "OXPXP", "PXXXO", "OXXXO", "OOOPP"], ["PXOPX", "OXOXP", "OXPXX", "OXXXP", "POOXX"], ["OOOXX", "XOOOX", "OOOXX", "OXOOX", "OOOOO"], ["PXPXP", "XPXPX", "PXPXP", "XPXPX", "PXPXP"]]))