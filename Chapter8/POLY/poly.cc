#include <iostream>
#include <string.h>
#include <algorithm>
#include <vector>
using namespace std;
int memo[101][101];
int n;
int poly(int, int);
int main(){
    int C;
    cin >> C;    
    for(int c=0; c<C; c++){
        memset(memo, -1, sizeof(memo));
        cin >> n;
        int sum = 0;
        for(int i=1; i<n+1; i++){
            sum+=poly(n, i);
        }
        if(sum>=10000000){
            sum%=10000000;
        }
        cout << sum << "\n";
    }
}

int poly(int n, int first){
    if(memo[n][first] != -1){
        return memo[n][first];
    }
    if(n == first){
        memo[n][first] = 1;
        return 1;
    }
    if(n == 2){
        if(first == 2){
            memo[2][2] = 1;
            return 1;
        }
        else if(first == 1){
            memo[2][1] = 1;
            return 1;
        }
    }
    int& ret = memo[n][first];
    ret = 0;
    for(int i=0; i<n-first; i++){
        ret += ((first + i)*poly(n-first, i+1))%10000000;
    }
    //cout << "n " << n << " first " << first << " ret " << ret << "\n"; for debug
    ret%=10000000;
    return ret;
}


