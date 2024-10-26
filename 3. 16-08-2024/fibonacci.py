# Código baseado de cálculo do n-ésimo fibonacci com o visto em aula


def main():
    n = int(input())
    ans = [[1, 1], [1, 0]]

    ans = matPow(ans, n)
    print(ans[0][1])
    return


def matPow(matrix, n):
    ans = [[1, 0], [0, 1]]
    while n:
        if n % 2:
            ans = matMul(ans, matrix)
        matrix = matMul(matrix, matrix)
        n //= 2
    return ans


def matMul(a, b):
    ans = [[0, 0], [0, 0]]
    mod = pow(10, 9) + 7
    for i in range(2):
        for j in range(2):
            for k in range(2):
                ans[i][j] += (a[i][k] % mod) * (b[k][j] % mod)
                ans[i][j] %= mod
    return ans


main()