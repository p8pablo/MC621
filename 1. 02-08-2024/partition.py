import math


def main():
    n, m = [int(x) for x in input().split()]
    arr = []
    r = math.sqrt(m) + 1
    r = math.ceil(r)
    for i in range(1, r + 1):
        if not (m % i) and i * n <= m:
            arr.append(i)
            if m // i * n <= m:
                arr.append(m // i)
    arr.sort()
    print(arr[-1])
    return


main()
