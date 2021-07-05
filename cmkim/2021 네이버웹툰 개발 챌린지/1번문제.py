def solution(lottery):
    answer = -1

    arr = [0] * 1001
    visited = [0] * 1001
    sum = 0
    count = 0
    for i in range(len(lottery)):
        if lottery[i][1] == 0 and visited[lottery[i][0]] == 0:
            arr[lottery[i][0]] += 1
        else:
            visited[lottery[i][0]] = 1

    for i in range(1000):
        if visited[i]:
            sum += arr[i]
            count += 1
    #print(sum, count)

    if sum:
        answer = (sum+count) // count
    else:
        answer = 0

    return answer