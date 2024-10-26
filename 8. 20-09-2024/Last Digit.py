# Usando função descrita na aula
def floydCycleFinding(x0):
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

def f(x0):
    x1 = x0 + 1
    num = x1 ** x1
    num %= 10
    return num
    


def main():
    while True:
        i = int(input())
        if not i:
            break
        num = floydCycleFinding(1)
        print(num)
    return
main()