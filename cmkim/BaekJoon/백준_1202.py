n, k = map(int, input().split())
jewel = [[0, 0] for _ in range(n)]
bag = [0 for _ in range(k)]
for i in range(n):
    jewel[i] = list(map(int, input().split()))

for i in range(k):
    bag[i] = int(input())

print(jewel)
print(bag)