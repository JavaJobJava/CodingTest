#CH5 BFS&DFS
#예제 5-5
# 팩토리얼

# 반복적으로 구현한 n!
def factorial_iteractive(n):
    result = 1
    for i in range(1,n+1):
        result*=i
    return result


# 재귀적으로 구현한 n!
def factorial_recursive(n):
    if n<=1:
        return 1
    #n!= n * (n-1)를 그대로 코드로 작성
    return n*factorial_recursive(n-1)

#n=5 일 경우 출력 
print('반복적으로 구현', factorial_iteractive(5))
print('재귀적으로 구현', factorial_recursive(5))
