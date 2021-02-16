#CH6 정렬
#예제 6-10
#위에서 아래로

#하나의 수열에는 다양한 수가 존재함. 이러한 수는 크기에 상관 없이 나열 되어 있음.
#이 수를 큰 수 부터 작은 수의 순서로 정렬해야 함. 수열을 내림차순으로 정렬하는 프로그램을 만드시오

N = int(input())
#N 크기의 리스트 초기화
num_list = [ 0 for _ in range(N)]
#정수 입력
for i in range(N):
    num_list[i]=(int(input()))
#내림차순 정렬
num_list.sort(reverse=True)

print(num_list)
    
