"""
@file imple-8.py
@brief 문자열 재정렬
@desc 구현, 문자열

1.
- 아스키코드 이용하여 알파벳/숫자 분류
+) 48-57 : 0~9 / 65~90 : A~Z / 97~122 : a~z
- list를 문자열로 변환 : "".join()

2.
- 알파벳 확인 함수 이용 : isalpha()
"""
s = input()

alphas = []
num = 0
# for c in s:
#     if c >= chr(65):
#         alphas.append(c)
#     else:
#         num += int(c)

for c in s:
    if c.isalpha():
        alphas.append(c)
    else:
        num += int(c)

alphas.sort()
alphas.append(str(num))
print("".join(alphas))
