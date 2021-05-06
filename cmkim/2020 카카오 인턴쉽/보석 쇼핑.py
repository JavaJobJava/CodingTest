def solution(gems):
    answer = []

    bosuck = []

    for i in gems:
        if i not in bosuck:
            bosuck.append(i)

    gems_count = len(gems)
    bosuck_count = len(bosuck)

    print(gems_count)

    switch = ([0] * bosuck_count for _ in range(gems_count))

    for i in range(gems_count):
        if gems[i] in bosuck:
            for j in range(bosuck_count):
                if gems[i] == bosuck[j]:
                    switch[i][j] = 1

    print(switch)



    return answer

'''
[1] [0] [0] [0]
[0] [1] [0] [0]
[0] [0] [1] [0]
[0] [0] [0] [1]
[0] [0] [1] [0]
[0] [0] [0] [0]
[0] [0] [0] [0]
[0] [0] [0] [0]


'''