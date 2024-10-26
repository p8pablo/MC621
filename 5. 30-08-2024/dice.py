def dice(n, a, b):
    max_sum = 6 * n
    dp = [[0] * (max_sum + 1) for _ in range(n + 1)]

    dp[0][0] = 1
    for i in range(1, n + 1):
        for s in range(i, max_sum + 1):
            for face in range(1, 7):
                if s - face >= 0:
                    dp[i][s] += dp[i - 1][s - face]

    prob = sum(dp[n][s] for s in range(a, b + 1))
    return prob


def main():
    n, a, b = map(int, input().split())
    sum = dice(n, a, b)
    total = 6**n
    print("{:.6f}".format(sum / total))
    return


main()
