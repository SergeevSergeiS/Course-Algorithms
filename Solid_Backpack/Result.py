l = [int(x) for x in input().split()]
w, n = l[0], l[1]
l = [int(x) for x in input().split()]
c = [1] + [0] * (w)
c_new = c[:]
for j in range(n):
    for i in range(l[j], w + 1):
        if c[i - l[j]] == 1:
            c_new[i] = 1
    c = c_new[:]
while c[w] == 0:
    w -= 1
print(w)
