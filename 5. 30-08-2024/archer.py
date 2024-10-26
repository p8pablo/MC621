def main():
    a, b, c, d =[int(x) for x in input().split()]
    small = a/b
    zanoes = c/d
    product = (1-small)*(1-zanoes)
    result = small/(1-product)
    print(f"{result:.12f}")

main()
