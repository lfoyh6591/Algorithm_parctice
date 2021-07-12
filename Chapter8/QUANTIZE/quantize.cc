#include <iostream>
#include <string.h>
#include <algorithm>
#include <vector>
using namespace std;
int memo[101][10];
int memo2[101][101];
int n, s;
vector<int> input;
int quantize(int, int);
int quantizeone(int, int);
int mean(int, int);
int main(){
    int C;
    cin >> C;    
    for(int c=0; c<C; c++){
        memset(memo, -1, sizeof(memo));
        memset(memo2, -1, sizeof(memo2));
        cin >> n;
        cin >> s;
        for(int i=0; i<n; i++){
            int k;
            cin >> k;
            input.push_back(k);
        }
        sort(input.begin(), input.end());
        int result = 987654321;
        for(int i=1; i<s+1; i++){
            result = min(result, quantize(0, i));
        }
        cout << result << "\n";
        input.clear();
    }
}

int quantize(int begin, int num){
    if(num>=n){
        memo[begin][num-1] = 0;
        return 0;
    }    
    if(memo[begin][num-1] != -1){
        return memo[begin][num-1];
    }
    if(num == 1){
        memo[begin][0] = quantizeone(begin, n);
        return memo[begin][0];
    }
    int ret = 987654321;
    for(int i=begin+1; i<n-num+1; i++){
        ret = min(ret, quantizeone(begin, i) + quantize(i, num-1));
    }
    memo[begin][num-1] = ret;
    // cout << "begin " << begin << " num " << num << " ret " << ret << " \n"; for debug
    return ret;
}

int quantizeone(int begin, int end){
    if(memo2[begin][end]!=-1){
        return memo2[begin][end];
    }
    int ret = 987654321;
    int retv = 0;
    int m = mean(begin, end);
    
    for(int j=begin; j<end; j++){
        retv += (m-input.at(j))*(m-input.at(j));
    }
    ret = min(ret, retv);
    retv = 0;

    memo2[begin][end] = ret;
    return ret;
}

int mean(int begin, int end){
    int sum = input.at(begin);
    for(int i=begin+1; i<end; i++){
        sum+=input.at(i);
    }
    return (int)(0.5+(double)sum/(end-begin));
}