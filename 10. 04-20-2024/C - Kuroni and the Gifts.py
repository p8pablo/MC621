def main():
    t = int(input())
    for _ in range(t):
        n = int(input())
        a = list(map(int, input().split()))
        b = list(map(int, input().split()))
        a.sort()
        found = False
        for order in [True, False]:
            b_sorted = sorted(b, reverse=not order)
            for k in range(n):
                x = a[:]
                y = []
                sums = set()
                valid = True
                for i in range(n):
                    index = (i + k) % n
                    yi = b_sorted[index]
                    s = x[i] + yi
                    if s in sums:
                        valid = False
                        break
                    sums.add(s)
                    y.append(yi)
                if valid:
                    print(' '.join(map(str, x)))
                    print(' '.join(map(str, y)))
                    found = True
                    break
            if found:
                break
    return
main()