stack =[]

stack.append(5)
stack.append(2)
stack.append(3)
stack.append(7)
stack.pop()
stack.append(1)
stack.append(4)
stack.pop()

# 5 2 3 7(pop) 1 4(pop)

print(stack) #넣은 순서대로 출력
print(stack[::-1]) # 스택 개념대로 위에서부터 출력

# stack[start index : end index : 출력방향]



