#include<bits/stdc++.h>
using namespace std;
string s;
int main() {
    cin >> s;
    int len = s.length(), ans = len / 2;
 
    if(len & 1) {
        for(int i = 1; i < len; ++i)
            if(s[i] == '1') {
                ++ans;
                break;
 
            }
    }
    cout << ans << endl;
 
    return 0;
}