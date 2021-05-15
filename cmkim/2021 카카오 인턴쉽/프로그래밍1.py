num = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']

def solution(s):
    answer = 0
    count = 0
    arr = []
    i = 0
    while i < len(s):


        if s[i].isdigit():
            arr.append(int(s[i]))

        else:
            j = 0

            while j < 10:
                if num[j] in s[i:i+5]:

                    arr.append(j)
                    i += len(num[j]) - 1
                    break
                j += 1
        i += 1

    answer = int("".join(map(str, arr)))
    print(answer)
    return answer

#solution('1zerotwozero3')


