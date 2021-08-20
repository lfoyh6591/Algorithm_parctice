#include <iostream>
#include <algorithm>
#include <vector>
#include <string>
using namespace std;
int memo[101][101];
int comparestring(int, int);
string W, S;
int main(){
    int c;
    cin >> c;
    for(int i=0; i<c; i++){
        cin >> W;
        int n;
        cin >> n;
        vector<string> file;
        for(int j=0; j<n; j++){
            cin >> S;
            for(int a=0; a<101; a++){
                for(int b=0; b<101; b++){
                    memo[a][b] = -1;
                }
            }
            if(comparestring(0, 0)>0){
                file.push_back(S);
            }
        }
        sort(file.begin(), file.end());
        for(int j=0; j<file.size(); j++){
            cout << file[j] << "\n";
        }
    }
}

int comparestring(int w, int s){
    if(memo[w][s]!=-1) { return memo[w][s]; }
    if((w==W.size()) && (s==S.size())){
        return 1;
    }
    
    if(w<W.size() && s<S.size() && ((W[w] == '?') || (W[w] == S[s]))){
        memo[w][s] = comparestring(w+1, s+1);
        return memo[w][s];
    }
    else if(W[w] == '*'){
        if(comparestring(w+1, s) || (s<S.size()) && comparestring(w, s+1)){
            memo[w][s] = 1;
            return memo[w][s];
        }
    }
    memo[w][s] = 0;
    return 0;
}
