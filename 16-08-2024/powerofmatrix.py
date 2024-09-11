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
    t = int(input())
    while(t):
        m, n = map(int, input().split())
        matrix = [[] for _ in range(m)]
        for i in range(m):
            matrix[i] = [int (x) for x in input().split()]
        ans = matPow(matrix, n, m)

        for i in range(m):
            print(*ans[i])
        t -= 1
    return
main()