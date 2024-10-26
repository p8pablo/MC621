# Usando função descrita na aula
def floydCycleFinding(x0):   
    if x0 == 1:
        return True 
    tortoise = f(x0)
    hare = f(f(x0))
    if tortoise == 1 or hare == 1:
        return True
    while tortoise != hare:
        tortoise = f(tortoise)
        hare = f(f(hare))
        if tortoise == 1 or hare == 1:
            return True
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
    return False

def f(x0):
    x1 = 0
    while x0:
        num = x0 % 10
        x1 += num ** 2
        x0 //= 10
    return x1

def main():
    num = int(input())
    for i in range(num):
        
        x = int(input())
        
        happy = floydCycleFinding(x)
        if happy:
            print(f"Case #{i+1}: {x} is a Happy number.")
        else:
            print(f"Case #{i+1}: {x} is an Unhappy number.")
        

main()