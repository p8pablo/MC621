#include <iostream>
#include <cmath>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(0);

    int n, x;
    cin >> n;

    for (int i = 0; i < n; i++) {
        cin >> x;
        int count = 0;

        for (int j = 1; j <= sqrt(x); j++) {
            if (x % j == 0) {
                count++;
                if (j != x / j) {
                    count++; 
                }
            }
        }

        cout << count << endl;
    }

    return 0;
}
