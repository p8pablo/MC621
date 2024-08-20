def main():
    n = int(input())
    s = input()
    for i in range(1, n):
        l = 0
        for j in range(n):
            if j + i < n and s[j] != s[j + i]:
                l = j + 1
            else:
                break
        print(l)

    return


main()
