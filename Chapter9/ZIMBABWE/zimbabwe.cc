#include <iostream>
#include <string.h>
#include <algorithm>
#include <vector>
using namespace std;
const int mod = 1000000007;
long long e;
int m;
int check[10];
int num1[15];
int n;
int result;
int memo[100];
void makenum(long long ,int, bool);
int main(){
    int C;
    cin >> C;
    for(int c=0; c<C; c++){
        memset(memo, -1, sizeof(memo));
        result = 0;
        cin >> e;
        cin >> m;
        long long e1 = e;
        n = 0;
        for(int i=0; i<10; i++){
            check[i] = 0;
        }
        while(e1 > 0){
            num1[n++] = e1%10;
            check[e1%10]++;
            e1/=10;
        }
        makenum(0, 0, true);
        if(e%m==0){
            result--;
        }
        cout << result << endl;
    }
}

void makenum(long long num, int length, bool issame){
    if(length == n){
        if(num%m == 0){
            result++;
            result%=mod;
            //cout << num << " num " << endl;
        }
    }
    if(issame){
        for(int i=0; i<=num1[n-length-1]; i++){
            if(check[i] != 0){
                if(i == num1[n-length-1]){
                    check[i]--;
                    makenum(num*10+i, length+1, true);
                    check[i]++;
                }
                else{
                    check[i]--;
                    makenum(num*10+i, length+1, false);
                    check[i]++;
                }
            }
        }
    }
    else{
        for(int i=0; i<10; i++){
            if(check[i] != 0){
                check[i]--;
                makenum(num*10+i, length+1, false);
                check[i]++;
            }
        }
    }
}