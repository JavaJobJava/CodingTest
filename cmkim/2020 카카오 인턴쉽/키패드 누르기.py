# 2, 5, 8, 0 의 경우 가장 최근의 왼손 오른손 위치 따지기 + 주손 따지기

def solution(numbers, hand):

    answer = ''
    left_cur = 0   # 양손의 위치 | 1, 4, 7, * 순으로 3, 2, 1, 0 에 대응한다
    left_hor = 1    # hor 값은 가로로 1, 2, 3 번째 줄 중 값중 하나

    right_cur = 0
    right_hor = 3

    mid_cur = 0
    mid_hor = 2


    for i in numbers:
        if i == 1 or i == 4 or i == 7 or i == '*':
            #print(left_cur, left_hor, right_cur, right_hor, mid_cur, mid_hor)
            answer += 'L'
            if i == 1:
                left_cur = 3
            if i == 4:
                left_cur = 2
            if i == 7:
                left_cur = 1
            if i == '*':
                left_cur = 0
            left_hor = 1

        if i == 3 or i == 6 or i == 9 or i == '#':
            #print(left_cur, left_hor, right_cur, right_hor, mid_cur, mid_hor)
            answer += 'R'
            if i == 3:
                right_cur = 3
            if i == 6:
                right_cur = 2
            if i == 9:
                right_cur = 1
            if i == '#':
                right_cur = 0
            right_hor = 3

        if i == 2 or i == 5 or i == 8 or i == 0:
            #print(left_cur, left_hor, right_cur, right_hor, mid_cur, mid_hor)
            if i == 2:
                mid_cur = 3
            if i == 5:
                mid_cur = 2
            if i == 8:
                mid_cur = 1
            if i == 0:
                mid_cur = 0
            mid_hor = 2

            left_d = abs(mid_cur - left_cur) + (mid_hor - left_hor)
            right_d = abs(mid_cur - right_cur) + (right_hor - mid_hor) #abs가 절댓값이였나?

            if left_d < right_d:
                answer += 'L'
                left_cur = mid_cur
                left_hor = 2
            elif left_d > right_d:
                answer += 'R'
                right_cur = mid_cur
                right_hor = 2
            else:
                if hand == 'left':
                    answer += 'L'
                    left_cur = mid_cur
                    left_hor = 2
                else:
                    answer += 'R'
                    right_cur = mid_cur
                    right_hor = 2

    return answer