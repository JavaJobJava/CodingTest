n = int(input())
time = list(map(int, input().split()))
result = 0
time.sort()

#print(time)

for i in range(0,n):
    result += (n-i)*time[i]

print(result)



