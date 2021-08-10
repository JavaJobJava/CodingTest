arr = input().split('-')
num = []

for i in arr:
    if '+' in i:
        sum = 0
        temp = i.split('+')

        for i in range(len(temp)):
            sum += int(temp[i])
    else:
        sum = i

    num.append(int(sum))

result = num[0]
if len(num) > 1:
    for i in range(1,len(num)):

        result -= num[i]

print(result)