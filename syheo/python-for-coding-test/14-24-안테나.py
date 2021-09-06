#CH14 정렬기출
#예제 14-24
#안테나
#백준 18310
#실버 3

# 아이디어 
# 중앙값에 위치한 값을 출력하면 안테나로부터 모든 집까지의 거리의 총합이 최소가 됨.
# 단 문제의 조건에서 가장 작은 위치 값을 출력하라 헀으니 짝수일때는 len(houses)//2-1 위치의 인덱스에 해당하는 값을 출력 

N = int(input())
houses = list(map(int,input().split()))
houses.sort()
print(houses[len(houses)//2-1]) if len(houses)%2==0 else print(houses[len(houses)//2])