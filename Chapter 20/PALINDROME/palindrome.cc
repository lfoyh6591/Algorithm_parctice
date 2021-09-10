#include <bits/stdc++.h>
using namespace std;

int palindrome_length(string s){
    int len = s.size();
    for(int i=0; i<len; i++){
        if(s[i] == s[len-1]){
            bool updated = true;
            for(int j=0; j<=(len-i)/2; j++){
                if(s[i+j]!=s[len-1-j]){
                    updated = false;
                    break;
                }
            }
            if(updated){
                return len+i;
            }
        }
    }
}

int main(){
    int C;    cin >> C;
    for(int c=0; c<C; c++){
        string s;
        cin >> s;
        cout << palindrome_length(s) << endl;
    }
}