n = int(input())
num = n
count = 0

while num > 0:
    num //= 100
    count += 1

temp = 10 ** count

left = n // temp
right = n % temp

Lresult = 0
Rresult = 0

for i in range(count):
    Lresult += left % 10
    Rresult += right % 10
    left //= 10
    right //= 10


if Lresult == Rresult:
    print("LUCKY")
else:
    print("READY")