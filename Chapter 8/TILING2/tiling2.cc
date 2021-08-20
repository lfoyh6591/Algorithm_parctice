#include <iostream>
#include <string.h>
#include <algorithm>
#include <vector>
using namespace std;
long long memo[100];
int n;
int tiling(int);
int main(){
    int C;
    cin >> C;    
    for(int c=0; c<C; c++){
        memset(memo, -1, sizeof(memo));
        cin >> n;
        cout << tiling(n) << "\n";
    }
}

int tiling(int m){
    if(memo[m-1] != -1){
        return memo[m-1];
    }
    if(m == 1){
        return 1;
    }
    if(m == 2){
        return 2;
    }
    memo[m-1] = (int)((long long)(tiling(m-1)+tiling(m-2))%1000000007);
    return memo[m-1];
}
