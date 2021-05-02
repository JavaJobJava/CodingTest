n = input()
result = []
sum = 0

for i in n:
    if 'A' <= i <= 'Z':
        result.append(i)
    else:
        sum += int(i)

result.sort()
if sum:
    result.append(str(sum))


print(''.join(result))


'''
K1KA5CB7
AJKDLSI412K4JSJ9D
'''