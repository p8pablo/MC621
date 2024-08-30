#include <iostream>
#include <vector>
#include <string>

using namespace std;

int main() {
    int n;
    cin >> n;
    vector<string> str;
    
    for (int i = 0; i < n; ++i) {
        int command;
        cin >> command;
        
        if (command == 1) {
            string s;
            cin >> s;
            str.push_back(s);
        } 
        else if (command == 2) {
            if (!str.empty()) {
                str.pop_back();
            }
        } 
        else if (command == 3) {
            string old_str, new_str;
            cin >> old_str >> new_str;
            for (int j = 0; j < str.size(); ++j) {
                if (str[j] == old_str) {
                    str[j] = new_str;
                }
            }
        }
    }
    
    if (!str.empty()) {
        for (const auto& s : str) {
            cout << s;
        }
    } else {
        cout << "The final string is empty" << endl;
    }

    return 0;
}
