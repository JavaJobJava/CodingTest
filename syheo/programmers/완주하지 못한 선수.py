#프로그래머스 
#고득점 Kit
#해시
#level1
#완주하지 못한 선수

def solution(participant, completion):
    answer = ''
    participant.sort()
    completion.sort()
    for i in range(len(completion)):
        if participant[i]!=completion[i]:
            return participant[i]
        
    return participant[-1]