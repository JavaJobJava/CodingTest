def main():

    t = int(input())

    for test in range(t):

        n, k = map(int, input().split()) #열 행 순서
        arr = [[0]*k for _ in range(n)] #같은 인덱스 안에서 움직이는게 쉬워서 가로세로 변경
        arr2= [[0]*k for _ in range(n)] #arr[i][j] = arr[i]행에서 arr[i][j]로 1을 옮기는 최소 횟수
                                        #arr[0~k][j] 값의 합의 최솟값구하기
        loc = [[] for _ in range(n)]
        answer = [0]*k
        result = n*k
        #print(loc)
        for i in range(k):
            temp = input()
            for j in range(len(temp)):
                if temp[j] == '1':
                    arr[j][i] = 1
                    loc[j].append((j, i))

        # print(loc)
        # for i in range(n):
        #     print(arr[i])

        for i in range(n):
            for j in range(k):
                min_v = k
                for p in range(len(loc[i])):
                    min_v = min(min_v, abs(loc[i][p][1] - j))
                    min_v = min(min_v, (j+k) - loc[i][p][1])
                arr2[i][j] = min_v

        # print('')
        # for i in range(n):
        #     print(arr2[i])

        for i in range(n):
            for j in range(k):
                answer[j] += arr2[i][j]


        # print('')
        # for i in range(k):
        #     print(answer[i])

        for i in range(k):
            result = min(result, answer[i])



        output = "#%d" % (test + 1)

        print(output, result)
main()