#include <iostream>
#include <string.h>
#include <algorithm>
#include <vector>
using namespace std;
int memo[101][10];
int memo2[101][101];
int psum[101], psqsum[101];
int n, s;
vector<int> input;
int quantize(int, int);
void precalc();
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
        precalc();
        int result = 987654321;
        for(int i=1; i<s+1; i++){
            result = min(result, quantize(0, i));
        }
        cout << result << "\n";
        input.clear();
    }
}

void precalc(){
    psum[0] = input[0];
    psqsum[0] = input[0]*input[0];
    for(int i=1; i<n; i++){
        psum[i] = psum[i-1] + input[i];
        psqsum[i] = psqsum[i-1] + input[i]*input[i];
    }
}


int quantize(int begin, int num){
    if(begin == n) return 0;
    if(num == 0) return 987654321;
    if(num>=n){
        memo[begin][num-1] = 0;
        return 0;
    }    
    if(memo[begin][num-1] != -1){
        return memo[begin][num-1];
    }
    /*if(num == 1){
        memo[begin][0] = quantizeone(begin, n-1);
        return memo[begin][0];
    }*/
    int ret = 987654321;
    for(int i=1; begin+i<=n; i++){
        ret  = min(ret, quantizeone(begin, begin+i-1)+quantize(begin+i, num-1));
    }
    /*for(int i=begin+1; i<n-num+1; i++){
        ret = min(ret, quantizeone(begin, i-1) + quantize(i, num-1));
    }*/
    memo[begin][num-1] = ret;
    //cout << "begin " << begin << " num " << num << " ret " << ret << " \n"; 
    return ret;
}

/*int quantizeone(int begin, int end){
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
}*/

int quantizeone(int begin, int end){
    int sum = psum[end] - (begin == 0 ? 0 : psum[begin-1]);
    int sqsum = psqsum[end] - (begin == 0 ? 0 : psqsum[begin-1]);

    int m = int(0.5 + (double)sum / (end - begin + 1));

    int ret = sqsum - 2*m*sum + m*m*(end-begin+1);
    //cout << "begin " << begin << " end " << end << " ret " << ret << " \n"; 
    return ret;
}

int mean(int begin, int end){
    int sum = input.at(begin);
    for(int i=begin+1; i<end; i++){
        sum+=input.at(i);
    }
    return (int)(0.5+(double)sum/(end-begin));
}