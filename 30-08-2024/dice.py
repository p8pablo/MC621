def main():
    n, a, b =[int(x) for x in input().split()]
    memo = {}
    soma = 0
    prob = dt(n, soma, a, b, memo)
    probtotal = 6**n
    sum = prob/probtotal
    sum = "{:.6f}".format(sum)
    print (sum)
    return
def dt(n, soma, a , b, memo):
    if n == 0 and (soma > b or soma < a):
        return 0
    if n == 0 and soma <= b and soma >= a:
        return 1
    
    prob = 0
    for i in range(1, 7):
        prob += dt(n-1, soma + i, a, b, memo)

    memo[(n,soma)] = prob
    return prob
main()