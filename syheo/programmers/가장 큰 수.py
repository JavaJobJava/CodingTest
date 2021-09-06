#프로그래머스 
#고득점 Kit
#그래프
#level2
#가장 큰 수

# level2 지만 
# 굉장히 어려웠다. 
# 일단 커스텀해야되는 정렬조건(단순한 대소 비교가 아닌)을 정렬에 적용해야 된다는 점
# cmp_to_key 가 있다는 사실도 처음 알게 되었고 
# 물론 나는 퀵정렬을 직접 구현하여 했지만 
# 퀵정렬이 장착된 기본 정렬 함수를 사용해도 된다
# 또한 신박한 코드를 봤다
'''
def solution(numbers):
    numbers = list(map(str, numbers))
    numbers.sort(key=lambda x: x*3, reverse=True)
    return str(int(''.join(numbers)))
'''
# 요 코드인데 이걸 어떻게 생각했을지 .. 대단하다 
# 아무튼 중요한 문제인듯!!


def sort_key(a,b):
    if int(str(a)+str(b))>int(str(b)+str(a)):
        return True
    else:
        return False

def quick_sort(array):
    #리스트가 하나 이하의 원소만을 담고 있다면 종료
    if len(array) <= 1:
        return array

    pivot = array[0] #피벗은 첫 번째 원소
    tail = array[1:] #피벗을 제외한 리스트 

    left_side = [x for x in tail if not sort_key(x,pivot)] # 분할된 왼쪽 부분
    right_side = [x for x in tail if sort_key(x,pivot)] # 분할된 오른쪽 부분

    #분할 이후 왼쪽 부분과 오른쪽 부분에서 각각 정렬을 수행하고, 전체 리스트를 반환
    return quick_sort(left_side) + [pivot] + quick_sort(right_side)

def solution(numbers):
    answer = ''
    numbers = list(reversed(quick_sort(numbers)))
    while len(numbers)>1 and numbers[0]==0:
        numbers=numbers[1:]
    return ''.join(list(map(str,numbers)))

# 풀이 2 # 

def sort_key(a,b):
    return (a,b) if int(str(a)+str(b))>int(str(b)+str(a)) else (b,a)


def solution2(numbers):
    answer = ''
    length = len(numbers)
    
    for i in range(length):
        for j in range(i+1,length):
            numbers[i],numbers[j] = sort_key(numbers[i],numbers[j])
    
    #print(numbers)
    answer = ''.join(list(map(str,numbers)))
    
    return answer

# 풀이 3 #

def solution3(numbers):
    answer = ''

    numbers.sort(reverse=True,key = lambda x: (str(x)[0],str(x)[1] if len(str(x))>1 else str(x)[0],str(x)[2] if len(str(x))>2 else str(x)[0],str(x)[3] if len(str(x))>3 else str(x)[0]))
    
    for i in range(len(list(map(str,numbers)))):
        if answer == '' and numbers[i]==0:
            pass
        else: 
            answer += ''.join(str(numbers[i]))
    
    
    return answer