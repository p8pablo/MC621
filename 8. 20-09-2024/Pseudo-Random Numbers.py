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
    num = 1
    while True:
        z,i,m,l = map(int, input().split())
        
        if z == l == i == m == 0:
            break
    
        f = lambda l: (z * l + i) % m
        
        lambda_ = floydCycleFinding(l, f)
        print(f"Case {num}: {lambda_}")
        num += 1

main()