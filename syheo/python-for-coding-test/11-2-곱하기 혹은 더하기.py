#CH11 그리디 기출
#예제 11-2
#곱하기 혹은 더하기

numbers = input()

result = 0
for num in numbers:
    num = int(num)
    if result <2 or num<2:
        result+=num
    else:
        result*=num
print(result)
    
