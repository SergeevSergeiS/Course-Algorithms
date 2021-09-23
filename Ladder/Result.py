n = int(input())
l = [0]
temp = list(input().split())
for i in range(n):
    l.append(int(temp[i]))
prev = 0
cur = l[1]
for i in range(2, n + 1):
    cur, prev = max(cur, prev) + l[i], cur
print(cur)
