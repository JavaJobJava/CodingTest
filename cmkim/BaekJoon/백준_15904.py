str= input()
compare = ['U', 'C', 'P', 'C']
count = 0


for i in range(len(str)):

    if compare[count] == str[i]:
        count += 1
    if count == 4:
        break

if count==4:
    print("I love UCPC")
else:
    print("I hate UCPC")

