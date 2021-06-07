import heapq

def solution(scoville, K):
    answer = 0
    heap = []
    for i in range(len(scoville)):
        heapq.heappush(heap, scoville[i])

    while heap[0] < K:
        if len(heap) < 2:
            return -1

        first = heapq.heappop(heap)
        second = heapq.heappop(heap)
        result = first + second * 2
        heapq.heappush(heap, result)
        answer += 1

    return answer