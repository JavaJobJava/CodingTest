"""
@file sort-23.py
@brief 국영수 (백준)
@desc
우선순위 함수 만들기
"""

import sys

n = int(sys.stdin.readline().rstrip())

students = []
for i in range(n):
    student = list(sys.stdin.readline().rstrip().split())
    students.append([student[0], int(student[1]), int(student[2]), int(student[3])])

students.sort(key=lambda x: (-x[1], x[2], -x[3], x[0]))

for student in students:
    print(student[0])
