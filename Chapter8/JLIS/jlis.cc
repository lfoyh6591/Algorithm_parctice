#include <iostream>
#include <vector>
#include <string.h>
using namespace std;
int input1[100];
int input2[100];
int memo[100][100];
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
        int maxv = 0;
        for(int i=0; i<n; i++){
            for(int j=0; j<m; j++){
                maxv = max(maxv, jlis(i, j));
            }
        }
        cout << maxv << "\n";
    }
}

int jlis(int index1, int index2){
    if(memo[index1][index2]!=0){
            cout << "index1 " << index1 << " index2 " << index2 << " ret " << memo[index1][index2] << "\n";

        return memo[index1][index2];
    }
    if((index1 == n-1) && (index2 == m-1)){
        if(input1[index1]!= input2[index2]){
            memo[index1][index2] = 2;
        }
        else{
            memo[index1][index2] = 1;
        }
            cout << "index1 " << index1 << " index2 " << index2 << " ret " << memo[index1][index2] << "\n";

        return memo[index1][index2];
    }

    int maxv = max(input1[index1], input2[index2]);
    int minv = min(input1[index1], input2[index2]);
    int ret = 2;
    
    for(int i=index1; i<n; i++){
        if((input1[i] > minv)){
            for(int j=index2; j<m; j++){
                if(input2[j] > minv){
                    ret = max(ret, jlis(i, j)+1);
                }
            }
        }
    }

    for(int i=index2; i<m; i++){
        if((input2[i] > minv)){
            for(int j=index1; j<n; j++){
                if(input1[j] > minv){
                    ret = max(ret, jlis(i, j)+1);
                }
            }
        }
    }
    memo[index1][index2] = ret;
    cout << "index1 " << index1 << " index2 " << index2 << " ret " << memo[index1][index2] << "\n";
    return memo[index1][index2];
}
