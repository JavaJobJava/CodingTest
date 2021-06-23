from _collections import deque

def main():

    t = int(input())

    for test in range(t):
        a, b, l = map(int, input().split())
        arr = list(map(str, input()))

        key1 = 0
        for i in range(len(arr)):
            if arr[i] == '+':
                key1 += pow(10, i)
            elif arr[i] == '-':
                key1 -= pow(10, i)

        key2 = 0
        arr.reverse()
        for i in range(len(arr)):
            if arr[i] == '+':
                key2 += pow(10, i)
            elif arr[i] == '-':
                key2 -= pow(10, i)

        key1, key2 = key2, key1

        print('')
        print('#case', test+1)
        print('key1, key2 = ', key1, key2)
        print('b-a = ', b-a)

        #raw값 구하는것부터 오류임
        if (b-a) % key1 == 0:
            raw1 = abs((a-b)//key1)

        elif (b-a) % key2 == 0:
            raw1 = abs((a-b)//key2)

        else:
            raw1 = -1
            answer = -1

        #print('raw1 = ', raw1)

        if raw1 > 0:
            count = len(str(raw1))#raw1의 자리수
            raw2 = pow(10, count) - raw1
            temp1, temp2 = 0, 1

            for i in range(count):
                temp1 += raw1 % 10
                temp2 += raw2 % 10
                raw1 = raw1 // 10
                raw2 = raw2 // 10

            print('temp1, temp2 = ', temp1, temp2)

            answer = min(temp1, temp2)
            # if not key1 * -1 == key2:
            #     answer = temp1

        output = "#%d" % (test + 1)
        print(output, answer)

def bfs(a, av, b, bv, target):
    arr_a = []
    arr_b = []
    while a < 1e6:
        arr_a.append(a)
        a *= 10
    while b < 1e6:
        arr_b.append(b)
        b *= 10

    # print(arr_a)
    # print(arr_b)



#main()

'''
5
159 555 2
+-
1142 350 3
+0-
116 676 2
+-
887 854 2
0-
370 994 2
+0
'''