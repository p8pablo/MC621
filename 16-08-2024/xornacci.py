def xor_inacci(a, b, n):
    if n % 3 == 0:
        return a
    elif n % 3 == 1:
        return b
    else:
        return a ^ b


def main():
    T = int(input())
    for _ in range(T):
        a, b, n = map(int, input().split())
        print(xor_inacci(a, b, n))


main()
