def solution(array, commands):
    arr = []
    answer = []
    example = len(commands)

    for i in range(example):
        start = commands[i][0]
        end = commands[i][1]
        count = commands[i][2]

        arr = array[start-1:end]
        arr.sort()

        #print(arr)

        answer.append(arr[count-1])

    return answer