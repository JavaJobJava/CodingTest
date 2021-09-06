def main():

    x, y = map(int, input().split())

    z = int(y * 100 / x)

    if z >= 99:
        print(-1)
        return 0

    answer = 1000000000
    start, end = 1, 1000000000
    while start <= end:
        mid = (start + end) // 2
        nextz = int((y + mid) * 100 / (x + mid))
        if z < nextz:
            if mid < answer:
                answer = mid
            end = mid - 1
        else:
            start = mid + 1

    print(answer)
main()