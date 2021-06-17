def solution(progresses, speeds):
    answer = []
    stack = []
    count = len(progresses)
    for i in range(count):
        div = (100-progresses[i])//speeds[i]
        if progresses[i] + div == 100:
            stack.append(div)
        else:
            stack.append(div+1)

    idx = stack[0]
    count = 1
    for i in range(1, len(stack)):
        if stack[i] > idx:
            answer.append(count)
            count = 1
            idx = stack[i]
        else:
            count +=1

    answer.append(count)


    return answer