def gcd(a, b):
    if b == 0: return a
    else: return gcd(b, a % b)

a, b = map(int, input().split())
c, d = map(int, input().split())

p = a * d + b * c
q = b * d

g = gcd(p, q)

print(p//g, q//g)