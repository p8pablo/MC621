def main():
    n, k =[int(x) for x in input().split()]
    sum = 0
    for i in range(1,n+1):
        count = 0
        value = i
        while (value < k):
            value *= 2
            count += 1
        sum += (1/n) * pow(0.5, count)
    sum = "{:.12f}".format(sum)
    print(sum)
    return
main()