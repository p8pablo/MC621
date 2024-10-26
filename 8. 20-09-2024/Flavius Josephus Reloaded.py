# Usando função descrita na aula
def floydCycleFinding(x0, f):
    # 1st part
    tortoise = f(x0)
    hare = f(f(x0))
    while tortoise != hare:
        tortoise = f(tortoise)
        hare = f(f(hare))
    # 2nd part
    mu = 0
    hare = x0
    while tortoise != hare:
        tortoise = f(tortoise)
        hare = f(hare)
        mu += 1
    # 3rd part
    lambda_ = 1
    hare = f(tortoise)
    while tortoise != hare:
        hare = f(hare)
        lambda_ += 1
    return lambda_

def main():
    while True:
        try:

            n, a, b = map(int,input().split())
            f = lambda x: (a*x*x + b) % n
            vivos_count = floydCycleFinding(0, f)
            print(n-vivos_count)
        except:
            break

    return
main()