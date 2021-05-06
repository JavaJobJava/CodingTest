# n가지 연산문자의 우선순위 재정의
# 무조건 n가지 우선순위가 있어야한다
# 음수는 절댓값으로 바꾸어 양수로 제출

def solution(expression):
    answer = 0

    arr = ''    #연산자 저장하는곳
    arr2 = ''
    num = []

    for i in range(len(expression)):
        if expression[i] == '+' or expression[i] == '-' or expression[i] == '*':
            #arr.append[i]
            arr += expression[i]
            #expression[i] = 0
    print(expression)
    # expression.replace('+', '.')
    # expression.replace('-', '.')
    # expression.replace('*', '.')
    table = str.maketrans('+-*', '...') #씨발련
    expression.translate(table)

    print(expression)

    arr2 = (expression.split('.'))

    print(arr2)

    return answer