a, b = map(int, input().split())
while b:     # while b != 0
    a, b = b, a % b
print(a)


#cheats
#from math import gcd
#print(gcd(*map(int, input().split())))
