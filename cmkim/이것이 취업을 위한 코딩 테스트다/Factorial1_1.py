def factorial(n):
    result = 1
    for i in range (1,n+1): # for ~ in range (,) 쓸 경우 range 의 범위는
                            # start index 없을땐 0부터 시작, last index-1 까지
        result *= i

    print(result)


factorial(3)
