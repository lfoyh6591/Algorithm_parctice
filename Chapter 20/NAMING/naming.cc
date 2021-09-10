#include <bits/stdc++.h>
using namespace std;
vector<int> result;
void solve(string s){
    int len = s.size();
    vector<int> match(len, 0);
    int begin = 1; 
    int matched = 0;
    int k;
    while(begin+matched < len){
        if(s[begin+matched] == s[matched]){
            match[begin+matched] = matched+1;
            matched++;
            if(matched == len-begin){
                result.push_back(matched);
            }
        }
        else{
            if(matched == 0)    begin++;
            else{
                begin += matched - match[matched-1];
                matched = match[matched-1];
            }
        }
    }
    while(match[matched-1]!=0){
        result.push_back(match[matched-1]);
        matched = match[matched-1];
    }
}

int main(){
    string father, mother;
    cin >> father >> mother;
    string s = father + mother;
    solve(s);
    reverse(result.begin(), result.end());
    for(auto it = result.begin(); it!=result.end(); it++){
        cout << *it << " ";
    }
    cout << s.length() << endl;
}