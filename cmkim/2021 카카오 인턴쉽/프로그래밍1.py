num = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']

def solution(s):
    answer = 0
    count = 0
    arr = []
    i = 0
    while i < len(s):
        #print('i = ', i)

        if s[i].isdigit():
            arr.append(int(s[i]))

        else:
            j = 0
            #print('i = ', i)
            # print(s[i:])
            while j < 10:
                if num[j] in s[i:i+5]:
                    #print('num[j] =', num[j])
                    arr.append(j)
                    i += len(num[j]) - 1
                    break
                j += 1
        i += 1

    #print(arr)
    answer = int("".join(map(str, arr)))
    #print('+'.join(arr))
    #answer = int("".join(arr))
    print(answer)
    return answer

#solution("one4seveneight")
solution('1zerotwozero3')

