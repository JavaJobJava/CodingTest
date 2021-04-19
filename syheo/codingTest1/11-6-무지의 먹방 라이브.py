#CH11 그리디 기출
#예제 11-6
#무지의 먹방 라이브
#카카오 신입 공채 2019 

#엄청 오래 걸림
#효율성 있게 하기 어려웠음.
import heapq

def keys(a):
    return a[1]

# food_times = [3,1,2]
# k=5
# food_times = [3, 2, 2, 1, 1, 2, 4, 5]
# k= 12
# food_times = [2, 2, 2, 1, 1, 2, 2, 2] 
# k= 14
# food_times = [7, 8, 3, 3, 2, 2, 2, 2, 2, 2, 2, 2]
# k = 35
food_times = [1, 6, 9, 3, 2, 5, 3, 2, 4, 4, 4, 7]
k = 26
def solution(food_times, k):
    answer = 0
    fixLength = len(food_times)
    length = fixLength
    rotation = 1
    curIdx = 0
    cnt = 0 
    for i in range(fixLength):
        food_times[i]=(food_times[i],i)
    food_times.sort()

    while k//length:
        k-=length
        cnt+=curIdx 
        while food_times[curIdx]==rotation:
            curIdx+=1
            length-=1
            if curIdx==len(food_times):
                return -1
        rotation+=1
        print(curIdx)

    food_times.sort(key=keys)
    print(food_times,k+cnt)
    answer = food_times[(k+cnt+1)%fixLength][1]+1
    
    answer += 1
     

    return answer


print(solution(food_times,k))