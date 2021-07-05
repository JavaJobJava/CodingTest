s = "one4seveneight"

dictionary = {}
dictionary['one']=1
dictionary['two']=2
dictionary['three']=3
dictionary['four']=4
dictionary['five']=5
dictionary['six']=6
dictionary['seven']=7
dictionary['eight']=8
dictionary['nine']=9
dictionary['zero']=0

def solution(s):
    answer = ''

    length = len(s)
    chk = ''
    for i in range(length):
        if s[i].isdigit():
            answer+=s[i]
        else:
            chk+=s[i]
        if chk in dictionary.keys():
            answer+=str(dictionary[chk])
            chk = ''
    
    return int(answer)

print(solution(s))