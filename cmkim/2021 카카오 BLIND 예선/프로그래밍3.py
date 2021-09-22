import math
def solution(fees, records):
    answer = []

    arr = [['']*3 for _ in range(len(records))]
    cars = ''
    for i in range(len(records)):
        t, n, c = records[i].split() #시간, 차 번호, 상태
        arr[i][0] += t
        arr[i][1] += n
        arr[i][2] += c
        if n not in cars:
            cars += n
            cars += ' '

    # for i in range(len(records)):
    #     print(arr[i])

    # print(cars)
    car = cars.split()
    #print(car)
    car.sort()# 자동차번호
    #print(car)
    time = [0 for _ in range(len(car))]  # 이용시간 저장
    money = [0 for _ in range(len(car))]
    for n in range(len(car)):#번호가 작은 차부터
        flag = 0 # 0=들어오기전, 1= 들어온상태
        s_time, e_time = 0, 0 #입차, 출차시간
        for i in range(len(records)):
            if car[n] == arr[i][1]:
                if flag == 1:
                    h, m = arr[i][0].split(':')
                    e_time = int(h) * 60 + int(m)
                    time[n] += e_time - s_time
                    flag = 0
                    continue
                if flag == 0:
                    h, m = arr[i][0].split(':')
                    s_time = int(h)*60 + int(m)
                    #print(h, m)
                    flag = 1
        if flag == 1:
            e_time = 1439
            time[n] += e_time - s_time

        if time[n] >= fees[0]:
            money[n] += fees[1]
            time[n] -= fees[0]
            money[n] += int(math.ceil(time[n] / fees[2]) *fees[3])
        else:
            money[n] += fees[1]

    print(money)


    return money

#solution([180, 5000, 10, 600], ["05:34 5961 IN", "06:00 0000 IN", "06:34 0000 OUT", "07:59 5961 OUT", "07:59 0148 IN", "18:59 0000 IN", "19:09 0148 OUT", "22:59 5961 IN", "23:00 5961 OUT"])