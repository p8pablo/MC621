def main():
    x = 1
    n = int(input())
    k = int(input())
    for i in range(n):
        if x * 2 > x + k:
            x = x + k
        else:
            x = x * 2
    print(x)
    return


main()
