#CH7 이진 탐색
#예제 7-8
#떡볶이 떡 만들기

# 떡볶이 떡의 길이가 다 다름.
# 절단기로 자를 경우 남는 떡만 가질 수 있음.

#떡의 개수, 떡의 길이 
N,M = map(int,input().split())
array = list(map(int,input().split()))

array.sort()

start = 0
end = array[N-1]
answer = 0

while True:
    if start > end: 
        break
    else:
        sum = 0
        mid = (start+end)//2
        for item in array:
            if item > mid:
                sum += item - mid
        if sum < M:
            end = mid - 1
        else:
            answer = mid
            start = mid +1

print(answer)
