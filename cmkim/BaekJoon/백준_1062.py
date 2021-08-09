def main():
    n = int(input())
    k = int(input())
    result = 0
    if k < 5:
        return result
    ord_cc = list(map(int, input().split())) # 후보 추천 순서

    frame = []
    score = []

    for i in range(k):
        if ord_cc[i] in frame:
            for j in range(len(frame)):
                if ord_cc[i] == frame[j]:
                    score[j] += 1
        else:
            if len(frame) >= n:
                for j in range(n):
                    if score[j] == min(score):
                        del frame[j]
                        del score[j]
                        break
            frame.append(ord_cc[i])
            score.append(1)
    # print(score)
    # print(frame)
    frame.sort()
    print(' '.join(map(str, frame)))

main()

