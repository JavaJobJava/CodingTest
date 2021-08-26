def solution(arr):
    arr.sort()
    dp = [0 for _ in range(255)]
    for i in range(0, 255):
        under, over = 0, 0
        for num in arr:
            if i > num:
                under += 1
            else:
                over += 1
        dp[i] = abs(under - over)

    for i in range(0, 255):
        if dp[i] == min(dp):
            answer = i

    # left = min(arr)
    # right = max(arr)
    # diff = len(arr)
    # print(diff)
    # under, over = 0, 0
    # while left < right:
    #     mid = (left + right) // 2
    #     for i in range(0, len(arr)):
    #         if mid < arr[i]:
    #             under = i
    #             over = len(arr) - i
    #             print('under, over = ', under, over)
    #             if abs(under - over) <= diff:
    #                 diff = abs(under - over)
    #                 answer = mid
    #             if under > over:
    #                 right = mid - 1
    #                 break
    #             elif under < over:
    #                 left = mid + 1
    #                 break
    #             else:
    #                 right -= 2
    #                 break
    #
    # return answer


arr =[0, 0, 255, 255, 0, 0, 255, 255, 255]
solution(arr)
