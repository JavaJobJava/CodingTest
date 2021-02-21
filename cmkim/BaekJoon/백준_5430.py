T = int(input())



for _ in range(T):                          #총 테스트 case
    func = input()                          #명령문 순서
    n = int(input())                        #몇개의 숫자
    n_count = n
    r_flag = 1                              # 1이 default -1은 reverse
    start = 0
    last = 0
    if n == 0:
        str=input()
        print('error')
    elif n > 0:
        arr = list(map(int, input()[1:-1].split(',')))   #숫자 리스트 입력

        for i in range(len(func)):
            if len(arr) > 0:
                if func[i] == 'R':
                    r_flag *= -1
                elif func[i] == 'D':
                    n_count -= 1
                    if r_flag == 1:
                        start += 1
                    else:
                        last += 1

        #print(start, end)

        if n_count < 0:
            print('error')
        elif n_count == 0:
            print('[]')
        elif r_flag == 1:
            #print(arr[start : n-end])
            print("[", end='')
            while start < n - last:
                print(arr[start], end='')
                if (start + 1 < n - last):
                    print(',', end='')
                start += 1
            print("]")

        else:
            arr.reverse()

            print("[", end='')
            while last < n-start:
                print(arr[last], end='')
                if(last+1 < n-start):
                    print(',', end='')
                last += 1
            print("]")

    else : print('error')



