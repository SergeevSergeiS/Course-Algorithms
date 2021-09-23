def diff(a, b):
    if a == b:
        return 0
    else:
        return 1


def main():
    a, b = input(), input()
    c = [[0] * (len(b) + 1) for i in range(len(a) + 1)]
    for i in range(len(a) + 1):
        c[i][0] = i
    for j in range(len(b) + 1):
        c[0][j] = j
    for i in range(1, len(a) + 1):
        for j in range(1, len(b) + 1):
            d = diff(a[i - 1], b[j - 1])
            x = (c[i - 1][j]) + 1
            y = (c[i][j - 1]) + 1
            z = (c[i - 1][j - 1]) + d
            if y >= x <= z:
                c[i][j] = x
            elif x >= y <= z:
                c[i][j] = y
            else:
                c[i][j] = z
    print(c[len(a)][len(b)])

if __name__ == '__main__':
    main()
