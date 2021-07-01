#include <iostream>
#include <vector>
#include <string.h>
using namespace std;
int memo[500];
int n;
int lis(int, vector<int>);
int main(){
    int c;
    cin >> c;    
    for(int i=0; i<c; i++){        
        cin >> n;
        memset(memo, 0, sizeof(memo));
        
        vector<int> sequence;
        for(int j=0; j<n; j++){
            int m;
            cin >> m;
            sequence.push_back(m);
        }
        int maxv = 0;
        for(int j=0; j<n; j++){
            maxv = max(maxv, lis(j, sequence));
        }
        cout << maxv << "\n";
    }
}
int lis(int index, vector<int> v){
    if(v.empty()){
        return 0;
    }
    if(memo[index]!=0){
        return memo[index];
    }
    if(index == 0){
        memo[0] = 1;
        return 1;
    }

    int maxv = 1;
    for(int i=index-1; i>=0 ; i--){
        if(v[index]>v[i]){
            maxv = max(maxv, lis(i, v)+1);
        }
    }
    memo[index] = maxv;
    return memo[index];
}
