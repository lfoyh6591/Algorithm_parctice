#include <iostream>
#include <algorithm>
#include <string.h>
using namespace std;
const long long NEGINF = numeric_limits<long long>::min();
int input1[100];
int input2[100];
int memo[101][101];
int n, m;
int jlis(int, int);
int main(){
    int C;
    cin >> C;    
    for(int c=0; c<C; c++){
        cin >> n;
        cin >> m;
        memset(memo, 0, sizeof(memo));

        for(int i=0; i<n; i++){
            cin >> input1[i];
        }
        for(int i=0; i<m; i++){
            cin >> input2[i];
        }
    
        cout << jlis(-1, -1) << "\n";
    }
}

int jlis(int index1, int index2){
    if(memo[index1+1][index2+1]!=0){
        return memo[index1+1][index2+1];
    }

    int result = 0;
    long long a = (index1 == -1 ? NEGINF : input1[index1]);
    long long b = (index2 == -1 ? NEGINF : input2[index2]);
    long long maxv = max(a, b);

    for(int i=index1+1; i<n; i++){
        if(input1[i] > maxv){
            result = max(result, jlis(i, index2) + 1);
        }
    }
    for(int i=index2+1; i<m; i++){
        if(input2[i] > maxv){
            result = max(result, jlis(index1, i) + 1);
        }
    }
    memo[index1+1][index2+1] = result;
    return result;
}