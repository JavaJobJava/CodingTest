'''
매일 k번이상
총합 2nk이상
'''

def solution(research, n, k):
    answer = ''
    arr = [[0]*26 for _ in range(len(research))]
    daily = [0 for _ in range(26)]
    total = [0 for _ in range(26)]
    succesion = [0 for _ in range(26)]

    for i in range(len(research)):
        for j in research[i]:
            arr[i][ord(j)-97] += 1

    # for i in range(len(research)):
    #     print(arr[i])

    for i in range(26):

        for a in range(len(research)-n+1):
            day = 0
            temp = 0
            for b in range(a, a+n):
                if arr[b][i] >= k:
                    day += 1
                    temp += arr[b][i]
                else:
                    day = 0
                    temp = 0

            if day >= n and temp >= 2*n*k: #이슈 검색어
                succesion[i] += 1
    #print(succesion)
    result = -1
    for i in range(26):
        if succesion[i] == max(succesion) and max(succesion)>0:
            result = i
            break
    #print(result)
    if result > -1:
        answer += chr(result+97)
    else:
        answer += 'None'

    return answer

