def main():
    t = int(input())#테스트케이스 개수

    for i in range(t):
        n = int(input())#낙타 마리수
        arr = list(map(int, input().split()))#낙타 이동시간 저장할 배열
        arr.sort()
        count = len(arr) #낙타의 총 마리수


        answer = 0
        if count >= 4:
            trans = arr[0] + arr[1] * 2

        while count > 0:

            if count >= 4:
                answer += (arr[count - 1] + trans)
                count -= 2

            elif count == 1:
                answer += arr[0]
                count -= 1

            elif count == 2:
                answer += arr[1]
                count -= 2

            elif count == 3:
                answer += (arr[0] + arr[1] + arr[2])
                count -= 3



        output = "#%d"%(i+1)


        print(output, answer)





main()