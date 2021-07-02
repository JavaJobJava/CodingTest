#프로그래머스 
#고득점 Kit
#스택/큐
#level2
#프린터

# 아이디어 
# 기존의 우선순위 리스트를 index와 값을 튜플로 가진 리스트로 변환하고 데크 자료형으로 변환시킴
# 그 후 우선순위를 비교하여 프린트함.
# iterable 객체에서 true 값이 하나라도 있으면 true를 반환해주는 any 메서드로 check_max_priority를 대체 할 수 있음 

from collections import deque

def check_max_priority(priorities,prior,index):
    for p,i in priorities:
        if p>prior:
            priorities.append((prior,index))
            return False
    return True


def solution(priorities, location):
    answer = 0
    
    priorities = deque([(priorities[i],i) for i in range(len(priorities))])
    
    while True:
        prior, index = priorities.popleft()
        if check_max_priority(priorities,prior,index):
            answer+=1
            if index == location:
                return answer   

# any 메서드 사용
def solution2(priorities, location):
    answer = 0
    
    priorities = deque([(priorities[i],i) for i in range(len(priorities))])
    
    while True:
        prior, index = priorities.popleft()
        if any([prior<priorities[i][0] for i in range(len(priorities))]):
            priorities.append((prior,index))
        else:
            answer+=1
            if index == location:
                return answer
                    
        