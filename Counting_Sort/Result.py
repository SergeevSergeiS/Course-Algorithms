def counting_sort(lst, n):
    c = [0] * 11
    for i in range(n):
        c[lst[i]] = c[lst[i]] + 1
    c[0] = c[0] - 1
    for i in range(1, 11):
        c[i] = c[i] + c[i - 1]
    result = [None] * n
    for x in reversed(lst):
        result[c[x]] = x
        c[x] = c[x] - 1
    return result
  

def main():
    n = int(input())
    lst = [int(x) for x in input().split()]
    result = counting_sort(lst, n)
    for i in range(len(result)):
        print(result[i], end = ' ')


if __name__ == '__main__':
    main()
