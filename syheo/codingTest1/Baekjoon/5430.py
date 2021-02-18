#solved.ac
#실버2
#구현
#AC
#5430

#선영이는 주말에 할 일이 없어서 새로운 언어 AC를 만들었다. AC는 정수 배열에 연산을 하기 위해 만든 언어이다. 이 언어에는 두 가지 함수 R(뒤집기)과 D(버리기)가 있다.

#함수 R은 배열에 있는 숫자의 순서를 뒤집는 함수이고, D는 첫 번째 숫자를 버리는 함수이다. 배열이 비어있는데 D를 사용한 경우에는 에러가 발생한다.

#함수는 조합해서 한 번에 사용할 수 있다. 예를 들어, "AB"는 A를 수행한 다음에 바로 이어서 B를 수행하는 함수이다. 예를 들어, "RDD"는 배열을 뒤집은 다음 처음 두 숫자를 버리는 함수이다.

#배열의 초기값과 수행할 함수가 주어졌을 때, 최종 결과를 구하는 프로그램을 작성하시오

from sys import stdin
import ast
from collections import deque

input = stdin.readline


is_error = False
#테스트 케이스 갯수
T = int(input())
#테스트 케이스 입력
for i in range(T):
    p = input()
    n = int(input())
    arr =ast.literal_eval(input())
    queue = deque(arr)
    sentence = ""
    cnt=0
    for cmd in p:
        if cmd =='\n':
            break
        if cmd=="R":
            cnt+=1
        elif cmd=="D":
            if len(queue)==0:
                is_error = True
                break
            elif cnt%2==0:
                queue.popleft()
            elif cnt%2==1:
                queue.pop()

    if len(queue)!=0:
        if cnt%2==1:
            queue.reverse()
        #문자열 제조
        sentence='['
        for i in range(len(queue)):
            sentence+=str(queue[i])
            if i!=len(queue)-1:
                sentence+=','
        
        sentence+=']'

    elif is_error:
        sentence="error"
    else : 
        sentence='[]'
    print(sentence)
    
        
    