"""
@file K번째수.py
@brief 정렬 - Level 1
@desc 
"""


def solution(array, commands):
    answer = []
    for i in commands:
        arr = sorted(array[i[0]-1:i[1]])
        answer.append(arr[i[2]-1])
    return answer
