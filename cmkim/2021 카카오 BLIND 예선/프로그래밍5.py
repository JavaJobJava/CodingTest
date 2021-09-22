# dp랑 플로이드 워셜?
# INF = 1e9
def floyd(arr, dp1, dp2, info):

    size = len(info)
    v1 = [[0] * size for _ in range(size)]
    v2 = [[0] * size for _ in range(size)]
    for i in range(size):
        for j in range(size):
            if arr[i][j]:   #j가 자식노드고
                if info[j]: #j가 늑대면
                    dp2[i][j] += 1
                    v2[i][j] = 1
                    # if dp1[i][j] <= dp2[i][j]:
                    #     dp1[i][j] = 0
                else:
                    dp1[i][j] += 1
                    v1[i][j] = 1
    for k in range(size):
        for i in range(size):
            for j in range(size):
                if arr[i][k] and arr[k][j] and not v1[i][k] and not v2[k][j]:
                    dp1[i][j] = dp1[i][k] + dp1[k][j] + dp1[i][j]
                    dp2[i][j] = dp2[i][k] + dp2[k][j] + dp2[i][j]
    for i in range(size):
        print(dp1[i])
    print('=====================')
    for i in range(size):
        print(dp2[i])
    print('=====================')

    dp3 = [[0] * size for _ in range(size)]
    for i in range(size):
        for j in range(size):
            dp3[i][j] = dp1[i][j] - dp2[i][i]
    for i in range(size):
        print(dp3[i])
    sum = 0
    for i in range(size):
        for j in range(size):
            if dp3[i][j] > 0:
                sum += dp3[i][j]
    return sum
def solution(info, edges):
    answer = 0
    size = len(info)
    # print(type(size))
    arr = [[0] * size for _ in range(size)]
    dp1 = [[0] * size for _ in range(size)] #양, 늑대
    dp2 = [[0] * size for _ in range(size)]
    #dp1[0][0] = 1
    #print(dp)


    # for i in range(size):
    #     arr[i][i] = INF
    #     print(arr[i])
    for i in range(len(edges)):
        a, b = edges[i][0], edges[i][1]
        # print('a, b = ',a, b)
        arr[a][b] = 1  # a의 자식은 b다
        arr[b][a] = 1
    # for i in range(size):
    #     print(arr[i])
    result = floyd(arr, dp1, dp2, info)

    return result

#solution([0,0,1,1,1,0,1,0,1,0,1,1], [[0,1],[1,2],[1,4],[0,8],[8,7],[9,10],[9,11],[4,3],[6,5],[4,6],[8,9]])