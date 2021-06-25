#solved.ac
#골드4
#그리디
#동전
#2091

# 1 센트 A 5센트 B 10센트 C 25센트 D
# X원 커피 동전을 최대로 사용


values = list(map(int,input().split()))
val = [1,5,10,25]
X = values[0]
#첫번째 요소 삭제
del values[0]

for value in values:
    flag = 0 
    index = values.index(value)
    for i in range(value,0,-1):
        money = X
        #동전 갯수가 들어갈 리스트 
        result = [0 for i in range(4)]
        
        #갯수 세기 
        for j in range(index+1,5):
            if money>=i*val[index]:
                money-=i*val[index]
                result[index]=i

                if money == 0:
                    flag = 1
                    break
            else:
                break
    if flag == 1: 
        print(result,seq=' ')
        break
    
        

