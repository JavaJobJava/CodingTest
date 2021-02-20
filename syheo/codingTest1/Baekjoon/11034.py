#solved.ac
#브론즈3
#그리디
#캥거루 세마리2
#11034

while True:
    try:
        kang = list(map(int,input().split()))
        print(kang[0])
        gap1 = kang[1]-kang[0]
        gap2 = kang[2]-kang[1]

        if gap1>gap2:
            print(gap1-1)
        else:
            print(gap2-1)
    except:
        break
    

    