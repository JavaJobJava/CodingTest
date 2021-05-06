n = int(input())

arr = []

for i in range (n):
    data = input().split()
    arr.append((data[0], int(data[1])))

arr = sorted(arr, key = lambda student:student[1]) #기본적으로 key 값을 기준으로 정렬하는데 람다식을 이용해
                                                   #values 값 기준으로 정렬할수 있게한다.

for student in arr:
    print(student[0], end = ' ')


#print(arr)