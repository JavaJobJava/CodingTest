#프로그래머스 
#고득점 Kit
#그래프
#level3
#순위 

# 이긴 횟수 + 진 횟수 = n-1 -> 결과 알 수 있음.

def solution(n, results):
    answer = 0
    players = [[] for _ in range(n+1)]
    victories = [set() for _ in range(n+1)]
    loses = [set() for _ in range(n+1)]
    
    for result in results:
        victories[result[0]].add(result[1])
        loses[result[1]].add(result[0])
    
    for i in range(1,n+1):
        #i한테 진애들은 i를 이긴 애들한테도 짐
        for loser in victories[i]:
            loses[loser].update(loses[i])
        #i를 이긴애들은 i한테 진애들도 이김
        for winner in loses[i]:
            victories[winner].update(victories[i])

    for i in range(1,n+1):
        if len(victories[i]) + len(loses[i]) == n-1:
            answer+=1

    
    return answer