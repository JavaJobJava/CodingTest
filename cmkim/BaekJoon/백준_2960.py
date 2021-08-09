n, k = map(int, input().split())
if n == 1:
    quit()
che = [False for _ in range(n+1)]
answer = []
#print(che)

count = 0
for i in range(2, (n+1)):
    if che[i]:
        continue
    count += 1
    che[i] = True
    if count == k:
        print(i)
        break
    for j in range(i+i, n+1, i):
        if not che[j]:
            che[j] = True
            count += 1
        if count == k:
            print(j)
            break

# 매우 비효율적인 코드인듯? 좀 더 줄일 수 있다.


#print(answer)

#print(che)
# for i in range(2, n+1):
#     if not che[i]:
#         answer.append(i)

#print(che)



