#CH11 그리디 기출
#예제 11-6
#무지의 먹방 라이브

def solution(food_times, k):
    answer = 0
    rotation = 1
    curIdx= 0 
    size = len(food_times)
    #계수 정렬 
    idxSorted = [0 for i in range(100000001)]
    for i in range(size):
        idxSorted[food_times[i]]+=1
    #퀵 정렬
    #food_times.sort()
    while True:
        if size<=0:
            answer = -1
            break
        elif k//size==0:
            answer = k+1
            break
        else:
            k-=size
            #퀵정렬시
            # while food_times[curIdx]==rotation:
            #     size-=1
            #     curIdx+=1
            size-=idxSorted[rotation]
            rotation+=1
            
                

    return answer