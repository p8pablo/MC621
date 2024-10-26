import math


def main():
    n = int(input())
    arr = []
    dist = []
    tree_num = 0
    for i in range(n):
        j = int(input())
        if i > 0:
            x = j - arr[-1]
            dist.append(x)
        arr.append(j)
    gcd = math.gcd(dist[0], dist[1])
    for i in range(2, len(dist)):
        gcd = math.gcd(gcd, dist[i])

    for i in range(n - 1):
        if dist[i] > gcd:
            tree_num += (dist[i] // gcd) - 1
    print(tree_num)
    return


main()
