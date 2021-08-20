#include<iostream>
#include<string>
#include<string.h>
using namespace std;
bool friends[10][10];
int n;
int findmatching(bool[]);
int main(){
    int testcase;
    cin >> testcase;

    for(int i=0; i<testcase; i++){
        int m;
        cin >> n;
        cin >> m;
        bool *matched = new bool[n];
        for(int j=0; j<10; j++){
            for(int k=0; k<10; k++){
                friends[j][k] = false;
            }
        }
        for(int j=0; j<m; j++){
            int a, b;
            cin >> a;
            cin >> b;
            friends[a][b] = true;
            friends[b][a] = true;
        }
        int result = findmatching(matched);
        
        cout << result << "\n";
    }
}

int findmatching(bool matched[]){
    int notmatched = -1;
    for(int i=0; i<n; i++){
        if(!matched[i]){
            notmatched = i;
            break;
        }
    }

    if(notmatched == -1){
        return 1;
    }

    int result = 0;
    for(int i=notmatched+1; i<n; i++){
        if(!matched[i] && friends[notmatched][i]){
            matched[notmatched] = true;
            matched[i] = true;
            result += findmatching(matched);
            matched[notmatched] = false;
            matched[i] = false;
        }
    }

    return result;
}