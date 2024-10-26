MOD = 10**9 + 7


def matMul(a, b, n):
    ans = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            for k in range(n):
                ans[i][j] = (ans[i][j] + a[i][k] * b[k][j]) % MOD
    return ans


def matPow(matrix, k, n):

    ans = [[1 if i == j else 0 for j in range(n)] for i in range(n)]

    while k:
        if k % 2 == 1:
            ans = matMul(ans, matrix, n)
        matrix = matMul(matrix, matrix, n)
        k //= 2
    return ans


def main():

    n, m, k = map(int, input().split())
    adj = [[0] * n for _ in range(n)]

    for _ in range(m):
        v_in, v_out = map(int, input().split())
        adj[v_in - 1][v_out - 1] += 1

    adj_k = matPow(adj, k, n)

    print(adj_k[0][n - 1] % MOD)
    return


main()
