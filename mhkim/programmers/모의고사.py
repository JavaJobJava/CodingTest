"""
@file 모의고사.py
@brief 완전탐색 - Level 1
@desc 
"""


def solution(answers):
    answer = []

    supoOne = [1, 2, 3, 4, 5]
    supoTwo = [2, 1, 2, 3, 2, 4, 2, 5]
    supoThree = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    correct = [0, 0, 0]

    for i in range(len(answers)):
        if answers[i] == supoOne[i % len(supoOne)]:
            correct[0] += 1
        if answers[i] == supoTwo[i % len(supoTwo)]:
            correct[1] += 1
        if answers[i] == supoThree[i % len(supoThree)]:
            correct[2] += 1

    for i in range(len(correct)):
        if correct[i] == max(correct):
            answer.append(i+1)

    answer.sort()
    return answer
