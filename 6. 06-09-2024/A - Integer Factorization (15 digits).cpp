#include <iostream>
#include <vector>
#include <bitset>
#include <cmath>
#include <map>

using namespace std;
// usando uma implementacao de Crivo de Eratóstenes como visto em aula
const int64_t sieve_size = 31622777;
bitset<1000000010> isprime;
vector<int64_t> primes;

void sieve(int64_t upperbound) {
    isprime.set();
    isprime[0] = isprime[1] = 0;
    for (int64_t i = 2; i <= sieve_size; i++) {
        if (isprime[i]) {
            for (int64_t j = i * i; j <= sieve_size; j += i) {
                isprime[j] = 0;
            }
            primes.push_back(i);
        }
    }
}

vector<int64_t> prime_factors(int64_t n) {
    vector<int64_t> factors;
    int64_t pf_idx = 0, pf = primes[pf_idx];
    
    while (pf * pf <= n) {
        while (n % pf == 0) {
            factors.push_back(pf);
            n /= pf;
        }
        pf = primes[++pf_idx];
    }
    
    if (n != 1) {
        factors.push_back(n);
    }
    
    return factors;
}

int main() {
    sieve(31622777);
    
    int64_t n;
    while (cin >> n && n != 0) {
        vector<int64_t> factors = prime_factors(n);
        
        int64_t last_factor = factors[0];
        int64_t e = 1;
        
        for (size_t i = 1; i < factors.size(); i++) {
            int64_t new_factor = factors[i];
            if (new_factor == last_factor) {
                e++;
            } else {
                cout << last_factor << "^" << e << " ";
                last_factor = new_factor;
                e = 1;
            }
        }
        cout << last_factor << "^" << e << endl;
    }

    return 0;
}
