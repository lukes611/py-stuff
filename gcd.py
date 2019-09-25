
def gcd(a, b):
    if a == 0 or b == 0: return 0
    if a == b: return a
    if a > b:
        return gcd(a - b, b)
    if b > a:
        return gcd(b - a, a)

print(gcd(0, 7))
print(gcd(-10, 7))