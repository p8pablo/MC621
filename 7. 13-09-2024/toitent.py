
def eulertotientcalc():
    MAX_N = 10**6
    phi = list(range(MAX_N + 1))
    for i in range(2, MAX_N + 1):
        if phi[i] == i:  
            for j in range(i, MAX_N + 1, i):
                phi[j] *= (i - 1)
                phi[j] //= i
    return phi
def main():
    phi = eulertotientcalc()
    t = int(input())
    for _ in range(t):
        n = int(input())
        print(phi[n])
    return
main()
