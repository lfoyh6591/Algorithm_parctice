#include <iostream>
#include <vector>
#include <string.h>
using namespace std;
int input1[100];
int input2[100];
int memo[100][100];
int n, m;
int main(){
    int C;
    cin >> C;    
    for(int c=0; c<C; c++){
        cin >> n;
        cin >> m;

        for(int i=0; i<n; i++){
            cin >> input1[i];
        }
        for(int i=0; i<m; i++){
            cin >> input2[i];
        }
    }
}

int jlis(int index1, int index2){
    if((index1 == n-1) && (index2 == m-1)){
        if(input1[index1]!= input2[index2]){
            memo[index1][index2] = 2;
        }
        else{
            memo[index1][index2] = 1;
        }
        return memo[index1][index2];
    }

    for(int i=index1; i<n; i++){
        for(int j=index2; j<m; j++){
            
        }
    }
}
