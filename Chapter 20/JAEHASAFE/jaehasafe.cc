#include <bits/stdc++.h>
using namespace std;

vector<int> get_partial(string a){
    int len = a.size();
    vector<int> matched(len, 0);

    int begin = 1, match = 0;
    while(begin+match<len){
        if(a[match] == a[begin+match]){
            matched[begin+match] = match+1;
            match++;
        }
        else{
            if(match == 0){
                begin++;
            }
            else{
                begin+=match - matched[match-1];
                match = matched[match-1];
            }
        }
    }
    return matched;
}

int rotate(string a, string b){
    b = b+b;
    int blen = b.size();
    int alen = a.size();

    vector<int> amatched = get_partial(a);
    int begin = 0, match = 0;
    
    while(begin+match<blen){
        if(a[match] == b[begin+match]){
            match++;    
            if(match == alen){
                return begin;
            }
        }
        else{
            if(match == 0){
                begin++;
            }
            else{
                begin += match-amatched[match-1];
                match = amatched[match-1];
            }
        }        
    }
    return 0;
}

int main(){
    int C;    cin >> C;
    for(int c=0; c<C; c++){
        int n;  cin >> n;
        string origin;  cin >> origin;
        int sum = 0;
        bool reverse = true;
        for(int i=0; i<n; i++){
            string target;  cin >> target;
            if(reverse){
                reverse = !reverse;
                sum+=rotate(origin, target);
                //cout << "1 rotate " << sum << endl;
                origin = target;
            }
            else{
                reverse = !reverse;
                sum+=rotate(target, origin);
                //cout << "2 rotate " << sum << endl;
                origin = target;
            }
        }
        cout << sum << endl;
    }
}