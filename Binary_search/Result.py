import sys

def find_pos(xs, query):
    low, high = 0, len(xs)
    while low < high:
        mid = (low + high) // 2
        if query < xs[mid]:
            high = mid
        elif query > xs[mid]:
            low = mid + 1
        else:
            return mid + 1
    return -1
def main():
    reader = (map(int, line.split()) for line in sys.stdin)
    n, *xs = next(reader)
    k, *queries = next(reader)
    for query in queries:
        print(find_pos(xs, query), end=' ')

if __name__ == '__main__':
    main()
