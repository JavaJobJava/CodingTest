"""
@file imple-7.py
@brief 럭키 스트레이트
@desc 구현, 문자열
"""
n = input()
before = 0
after = 0
for i in range(0, len(n)//2):
    before += int(n[i])
for i in range(len(n)//2, len(n)):
    after += int(n[i])

if before == after:
    print("LUCKY")
else:
    print("READY")
