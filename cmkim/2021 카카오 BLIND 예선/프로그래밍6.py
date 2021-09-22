def solution(board, skill):
    answer = 0
    r = len(board)
    c = len(board[0])

    for i in range(len(skill)):
        type, r1, c1, r2, c2, num = skill[i]
        #print(type, r1, c1, r2, c2, num)
        if type == 1:
            for i in range(r1, r2+1):
                for j in range(c1, c2+1):
                    board[i][j] -= num
        else:
            for i in range(r1, r2+1):
                for j in range(c1, c2+1):
                    board[i][j] += num

    for i in range(r):
        for j in range(c):
            if board[i][j]>0:
                answer += 1

    return answer