#CH5 BFS&DFS
#예제 5-4
# 재귀함수 종료

def recursive_function(i):
    #100번째 출력했을 때 종료하도록 종료조건 명시
    if i==100:
        return
    print(i,'번째',' 재귀 함수를 호출합니다.')
    recursive_function(i+1)
    print(i,'번째',' 재귀 함수를 종료합니다.')

recursive_function(1)
