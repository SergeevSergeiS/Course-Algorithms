n, m = map(int, input().split())
o, i = [0,1], 2
while not (o[i-2] == 0 and o[i-1] == 1) or i <= 2:
	o.append((o[i-2] + o[i-1]) % m)
	i += 1
print(o[n % (i-2)])
