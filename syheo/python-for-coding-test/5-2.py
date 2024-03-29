#CH5 BFS&DFS
#예제 5-2
# 큐
# 삽입(5)-삽입(2)-삽입(3)-삽입(7)-삭제()-삽입(1)-삽입(4)-삭제()

from collections import deque

#큐(Queue) 구현을 위해 deque 라이브러리 사용
queue = deque()

#구현
queue.append(5)
queue.append(2)
queue.append(3)
queue.append(7)
queue.popleft() #가장 먼저 들어온 원소 제거 
queue.append(1)
queue.append(4)
queue.popleft()

print(queue) #먼저 들어온 순서대로 출력
queue.reverse() #다음 출력을 위해 역순으로 바꿈
print(queue) #역순 출력

