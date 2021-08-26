def solution(card_numbers):
    answer = []
    for card in card_numbers:
        arr = card.split('-')
        result = 0
        #print(arr)
        valid = 1
        print(len(arr))
        if len(arr) == 4:
            for i in range(4):
                if len(arr[i]) != 4:
                    valid = 0

            if valid == 0:
                answer.append(0)
                continue

            for i in range(4):
                for j in range(4):
                    result += int(arr[i][j])
                    if j%2 == 0:
                        result += int(arr[i][j])
            if result % 10 == 0:
                answer.append(1)
            else:
                answer.append(0)
        else:
            for i in range(16):
                result += int(arr[i])
                if i % 2 == 0:
                    result += int(arr[i])
            if result % 10 == 0:
                answer.append(1)
            else:
                answer.append(0)
    return answer