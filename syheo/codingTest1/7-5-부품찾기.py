#CH7 이진 탐색
#예제 7-5
#부품 찾기 

# 부품 N개 -> 고유 번호 정수 
# 손님 M개 
# 있으면 yes 없으면 no 출력 

#이진 탐색
def binary_search(array,start,end,target):
    while True :
        if start>end:
            return 'no'
        else:
            mid = (start+end)//2
            if array[mid]==target:
                return 'yes' 
            elif array[mid]<target:
                start = mid+1
            elif array[mid]>target:
                end = mid-1
        

#부품과 번호 입력 
N = int(input())
array = list(map(int,input().split()))
#정렬 
array.sort()
# 손님 구매 갯수, 번호 
M = int(input())
targets = list(map(int,input().split()))

#부품 존재 여부 찾기 
for i in range(M):
    print(binary_search(array,0,N-1,targets[i]),end=' ')



