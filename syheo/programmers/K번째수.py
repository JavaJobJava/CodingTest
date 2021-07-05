#프로그래머스 
#고득점 Kit
#정렬
#level1
#k번째수

def solution(array, commands):
    answer = []
    
    for cmd in commands:
        tmp_array = sorted(array[cmd[0]-1:cmd[1]])
        answer.append(tmp_array[cmd[2]-1])
    return answer