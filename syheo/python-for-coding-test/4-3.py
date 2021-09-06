#CH4 구현
#예제 4-3
#왕실의 나이트

# 8*8 왕실 
# 이동 방향 경우의 수 리스트에 넣고 
# for 문 돌려서 다음 위치 값 out of index인지 확인 

row = [1,2,3,4,5,6,7,8]
col = ['a','b','c','d','e','f','g','h']

cnt = 0
# dict 사용안하고 tuple 사용했어도 됐다 
cases = [{1:2},{-1:2},{1:-2},{-1:-2},{2:1},{-2:1},{2:-1},{-2:-1}]

#위치 입력
loc= input()

#행, 열 인덱스 값으로 설정
c = col.index(loc[0])
r = row.index(int(loc[1]))


for case in cases:
    for key, val in case.items():
        #다음 위치값 
        ctmp=c+key
        rtmp=r+val
        #이동 가능여부 확인 
        if ctmp>=0 and ctmp<8 and rtmp>=0 and rtmp<8:
            cnt+=1

print(cnt)


