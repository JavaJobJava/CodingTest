#CH8 동적 프로그래밍
#예제 8-3
#호출 확인

d = [0] * 100

def pibo(x):
    print('f(' + str(x) + ')',end=' ')
    if x==1 or x==2:
        return 1
    if d[x]!= 0:
        return d[x]
    d[x] = pibo(x-1)+pibo(x-2)
    return d[x]

pibo(6)