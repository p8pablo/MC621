#include <iostream>
#include <vector>
#include <string>
using namespace std;

bool convert(int n, int k, string a, string b) {
    vector<int> freqA(26, 0), freqB(26, 0);

    for (char c : a) {
        freqA[c - 'a']++;
    }
    for (char c : b) {
        freqB[c - 'a']++;
    }

    for (int i = 0; i < 25; ++i) { 
        if (freqA[i] < freqB[i]) {
            return false; 
        }
        
        int excess = freqA[i] - freqB[i];
        if (excess % k != 0) {
            return false; 
        }
        freqA[i + 1] += excess; 
    }

    
    return freqA[25] == freqB[25];
}
int main(){
    int t;
    cin >> t;
    while(t--)
    {
        int n, k;
        string a, b;
        cin >> n >> k >> a >> b;
        if(convert(n,k,a,b)){
            cout << "Yes" << endl;
        }
        else
        {
            cout << "No" << endl;
        }
        
    }
    
    return 0;
}