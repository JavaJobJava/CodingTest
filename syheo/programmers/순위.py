#프로그래머스 
#고득점 Kit
#그래프
#level3
#순위 

# 이긴 횟수 + 진 횟수 = n-1 -> 결과 알 수 있음.

# 야매 풀이 

def solution(n, results):
    answer = 0
    players = [[] for _ in range(n+1)]
    victories = [set() for _ in range(n+1)]
    loses = [set() for _ in range(n+1)]
    
    for result in results:
        victories[result[0]].add(result[1])
        loses[result[1]].add(result[0])
    

    for result in results:
        for loser in victories[result[1]]:
            loses[loser].add(result[0])
            victories[result[0]].add(loser)
        for winner in loses[result[0]]:
            victories[winner].add(result[1])
            loses[result[1]].add(winner)
            

    for result in results:
        for loser in victories[result[1]]:
            loses[loser].add(result[0])
            victories[result[0]].add(loser)
        for winner in loses[result[0]]:
            victories[winner].add(result[1])
            loses[result[1]].add(winner)
        

    for i in range(1,n+1):
        if len(victories[i]) + len(loses[i]) == n-1:
            answer+=1

    
    return answer