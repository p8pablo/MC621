#include <iostream>
#include <vector>
#include <unordered_set>
#include <string>

using namespace std;

void solve() {
    int t;
    cin >> t;
    
    while (t--) {
        int n;
        cin >> n; 
        
        vector<string> strings(n);
        unordered_set<string> string_set;
        
        for (int i = 0; i < n; i++) {
            cin >> strings[i];
            string_set.insert(strings[i]);
        }
        
        string result = "";
        
        for (const string& s : strings) {
            bool found = false;
            for (int i = 1; i < s.size(); i++) { 
                string prefix = s.substr(0, i);
                string suffix = s.substr(i);
                if (string_set.find(prefix) != string_set.end() && string_set.find(suffix) != string_set.end()) {
                    found = true;
                    break;
                }
            }
            if (found) {
                result += '1';
            } else {
                result += '0';
            }
        }
        
        cout << result << endl;
    }
}

int main() {
    
    solve();
    
    return 0;
}
