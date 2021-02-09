#solved.ac
#브론즈3
#그리디
#UCPC는 무엇의 약자일까?
#15904

sentence = input()

answer = "I love UCPC"
wrong = "I hate UCPC"

ucpc = ['U','C','P','C']
index = 0

for word in sentence:
    if word==ucpc[index]:
        index+=1
    if index==4:
        break

if index==4:
    print(answer,end="")
else:
    print(wrong,end="")

