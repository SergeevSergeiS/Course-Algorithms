#no tree this time
n, w = map(int, input().split())
y, letters, x, temp, str = [], {}, 0, '', ''
for i in range(0,n):
    y.append(input())
z = input()
for i in range(len(y)):
    letters[y[i][3:]] = y[i][0]
while x < w:
    temp += z[x]
    if temp in letters:
        str += letters[temp]
        temp = ''
        x += 1
    else:
        x += 1
print(str)
