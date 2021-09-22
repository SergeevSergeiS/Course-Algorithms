import sys
from bisect import bisect_left, bisect_right

def main():
    reader = (map(int, line.split()) for line in sys.stdin)
    temp = list(next(reader))
    no, nt = temp[0], temp[1]
    begs = []
    ends = []
    for i in range(0, no):
        temp = list(next(reader))
        begs.append(temp[0])
        ends.append(temp[1])
    pois = list(next(reader))

    begs.sort()
    ends.sort()
    
    for i in range(nt):
        print(bisect_right(begs, pois[i])  - bisect_left(ends, pois[i]), end=' ')



if __name__ == '__main__':
    main()
