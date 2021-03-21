#CH6 정렬
#예제 6-11
#성적이 낮은 순서로 학생 출력하기

# N명의 학생 정보가 있음 학생 정보는 학생의 이름과 학생의 성적으로 구분됨.
# 각 학생의 이름과 성적 정보가 주어졌을 때 성적이 낮은 순서대로 학생의 이름을 출력하는 프로그램을 작성하시오 

# N 입력
N = int(input())
info = []
# 값 입력 
for i in range(N):
    tmp = input().split()
    info.append(tmp)

def set_key(value):
    return value[1]

info.sort(key=set_key)
# lambda 사용
# info = sorted(info, key = lambda value: value[1])

for i in range(N):
    print(info[i][0],end=' ')