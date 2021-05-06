from collections import deque


queue = deque()

queue.append(5)
queue.append(2)
queue.append(3)
queue.append(7)
queue.popleft()
queue.append(1)
queue.append(4)
queue.popleft()

# 5(pop) 2(pop) 3 7 1 4

print(queue)
queue.reverse()
print(queue)
print(queue[0]) #indexing 출력은 된다.
#print(queue[0:3])  queue는 stack 과 다르게 슬라이싱이 안된다.