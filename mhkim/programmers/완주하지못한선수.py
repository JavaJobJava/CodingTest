def solution(participant, completion):
    answer = ''

    names = dict()
    for p in participant:
        if p in names:
            names[p] += 1
        else:
            names[p] = 1

    for c in completion:
        names[c] = names[c]-1

    for n in names:
        if names[n] == 1:
            answer = n

    return answer