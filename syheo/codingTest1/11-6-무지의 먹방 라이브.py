#CH11 그리디 기출
#예제 11-6
#무지의 먹방 라이브


arr = [1,2,3,4]

for a in arr:
    print(a)
    if a==2:
        
        arr.pop(arr.index(a))
