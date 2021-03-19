s = int(input())

for i in range(1, s+1):
    if i*(i+1)//2 > s:
        result = i-1
        break

print(result)