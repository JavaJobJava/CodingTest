import heapq

n = int(input())
heap = []

for i in range(n):
    data = int(input())
    heapq.heappush(heap, data)

result = 0

while len(heap) != 1:
    a = heapq.heappop(heap)
    b = heapq.heappop(heap)
    sum = a + b
    result += sum
    heapq.heappush(heap, sum)

print(result)

# n = int(input())
#
# arr = []
#
# for i in range(n):
#     arr.append(int(input()))
#
# arr.sort()
#
#
#
# if n > 1:
#     answer = arr[0] + arr[1]
#     for i in range(2, n):
#         answer += answer
#         answer += arr[i]
#         #print('answer = ', answer)
#
# if n < 2:
#     answer = arr[0]
#
# print(answer)
'''
10
20 30
30 60  90
40 100 190 280
50 150 340 
60 210 550
70 280

10
20 
40 
50 

60 180
'''