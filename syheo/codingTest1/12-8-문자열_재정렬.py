#CH12 구현 기출
#예제 12-8
#문자열 재정렬
#페이스북 인터뷰

string = list(input())

string.sort()
sum = 0

for i in range(len(string)):
    if string[i].isdigit():
        sum+=int(string[i])
    else:
        break
string = string[i:]
string.append(str(sum))

print(''.join(string))