T = int(input())

for _ in range(T):
    n = int(input())
    arr = [] * (n+1)
    arr = list(map(int, input().split()))

    left, right = 0, 0

    for i in range(n):
        for j in range(n):
            if i+1 == arr[j] and i < j:
                left = max(left, j-i)

            if i+1 == arr[j] and i > j:
                right = max(right, i-j)

    if left + right:
        print(left+right-1)
    else:
        print(0)


'''
1 2 3 4 5 


1 5 3 4 2



4 5 3 2 1
4 3 5 2 1
3 4 5 2 1
3 4 2 5 1
3 2 4 5 1
2 3 4 5 1
2 3 4 1 5
2 3 1 4 5
2 1 3 4 5
1 2 3 4 5

4 5 3 2 1
3 5 4 2 1
2 5 4 3 1
1 5 4 3 2
1 4 5 3 2
1 3 5 4 2
1 2 5 4 3
1 2 4 5 3
1 2 3 5 4
1 2 3 4 5



1 2 3
 -
3 2 1
'''