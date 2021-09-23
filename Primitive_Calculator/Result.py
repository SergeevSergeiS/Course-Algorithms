n = int(input()) + 1
D = [n for i in range(n)]
D[1] = 1
for i in range(1, n):
    for k in [i * 2, i * 3, i + 1]:
        if k < n and D[k] > D[i] + 1:
            D[k] = D[i] + 1
n -= 1
A = [n]
while n != 1:
    a1 = [D[n - 1], n - 1]
    a2 = [D[n // 3], n // 3] if n % 3 == 0 else [n]
    a3 = [D[n // 2], n // 2] if n % 2 == 0 else [n]
    a = min(a1, a2, a3)
    A.append(a[1])
    n = a[1]
A.reverse()
print(D[-1] - 1)
print(*A)
