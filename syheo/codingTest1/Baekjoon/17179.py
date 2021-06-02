#solved.ac
#실버1
#이분탐색
#케이크 자르기
#17179

N,M,L = map(int,input().split())

cuts = [0,L]
cnts = []
pieces = []

#자를 수 있는 지점 입력
for i in range(M):
    cuts.append(int(input()))
cuts.sort()
#조각내기
for i in range(1,len(cuts)):
    pieces.append(cuts[i]-cuts[i-1])
print(pieces)
#목록 입력 
for i in range(N):
    cnts.append(int(input()))
answers = []

while cnts:
    left = 0
    right = L
    mid = (left+right)//2
    answer = 0
    cnt = cnts.pop(0)+1
#10 10 15 20 5 10 
    while left<=right and (left+right)//2!=0:
        cmpCnt = 0 
        minValue = int(1e9)
        idx = 0
        sum = 0
        sumList = []
        mid = (left+right)//2
        #print(cnt,left,right,mid)
        # 롤케이크 조각 내기 
        while idx!=len(pieces):
            sum = 0
            #print(idx,sum,mid)
            while idx!= len(pieces) and sum<mid:
                sum+= pieces[idx]
                idx+=1
            if sum>=mid:
                sumList.append(sum)
                cmpCnt+=1
                #print(sumList,cnt)
        minValue=min(sumList)
        #print('cmpCnt:',cmpCnt)
        if cmpCnt>cnt:
            left=mid+1
        elif cmpCnt<cnt:
            right = mid-1
        else:
            #
                #print('남은조각',sum,mid)
            right=mid-1
            answer=max(minValue,answer)
    answers.append(answer)

for answer in answers:
    print(answer)
