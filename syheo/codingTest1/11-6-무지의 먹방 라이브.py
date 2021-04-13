#CH11 그리디 기출
#예제 11-6
#무지의 먹방 라이브
import heapq

# food_times = [3,1,2]
# k=5
# food_times = [3, 2, 2, 1, 1, 2, 4, 5]
# k= 12
food_times = [2, 2, 2, 1, 1, 2, 2, 2]
k= 14
def solution(food_times, k):
    answer = 0
    rest = k
    length = len(food_times)
    rotation = 1
    q = []
    for i in range(length):
        heapq.heappush(q,(food_times[i],i))

    while True:
        if  q and rest//len(q):  
            rest-=1*len(q)
            while q and q[0][0]==rotation:
                heapq.heappop(q)
            rotation+=1
        else:
            q.sort(key=lambda x : x[1])
            
            if len(q)==0:
                answer = -1
            elif rest>=len(q):
                answer = q[rest-len(q)][1]
            else:
                answer = q[rest][1]+1
            break

    return answer


print(solution(food_times,k))