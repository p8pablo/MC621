def maxp(n):
    p = 0
    while n != 1:
        n//=2
        p += 1
    return p 
def carta_sobrando(n):
    if n == 1:
        return 1
    p = 2 ** maxp(n) 
    return 2 * (n - p)

def main():
    while True:
        x = int(input())
        if not x:
            break
        carta = carta_sobrando(x)
        print(carta)
main()