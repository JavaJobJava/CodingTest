#프로그래머스 
#고득점 Kit
#완전 탐색
#level1
#모의고사

def solution(answers):
    firstList = [1,2,3,4,5]
    secondList = [2, 1, 2, 3, 2, 4, 2, 5]
    thirdList = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    
    persons = [0 for _ in range(3)]
    
    for i in range(len(answers)):
        if answers[i] == firstList[i%5]:
            persons[0] += 1
        if answers[i] == secondList[i%8]:
            persons[1] += 1
        if answers[i] == thirdList[i%10]:
            persons[2] += 1
    maxCnt = max(persons)
    answer = []
    
    for i in range(3):
        if persons[i]==maxCnt:
            answer.append(i+1)
    return answer