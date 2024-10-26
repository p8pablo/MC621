#define MAXDIGITS 100
#define PLUS 1
#define MINUS -1
#include <iostream>
#include <cstring>

using namespace std;


typedef long long ll;
struct bignum
{
    char digits[MAXDIGITS];
    int signbit;
    int lastdigit;
};


void ll_to_bignum(long long s, bignum *n) {
    int i;
    long long t;

    // Define o sinal do número
    if (s >= 0) {
        n->signbit = PLUS;
    } else {
        n->signbit = MINUS;
    }

    // Inicializa os dígitos com zero
    for (i = 0; i < MAXDIGITS; i++) {
        n->digits[i] = (char) 0;
    }

    n->lastdigit = -1;

    // Obtém o valor absoluto
    t = (s >= 0) ? s : -s;

    // Converte o número para a representação em dígitos
    while (t > 0) {
        n->lastdigit++;
        n->digits[n->lastdigit] = (char) (t % 10);
        t = t / 10;
    }

    // Caso o número seja zero
    if (s == 0) {
        n->lastdigit = 0;
    }
}

int main() {
    int n;
    cin >> n;
    for (int i = 0; i < n; i++)
    {
        ll num1,num2;
        cin >> num1;
        cin >> num2;
        bignum n1;
        bignum n2;
        ll_to_bignum(num1, &n1);
        ll_to_bignum(num2, &n2);

    }
    


    return 0;
}
