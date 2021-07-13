#include <iostream>
#include <vector>
#include <string.h>
using namespace std;
int memo[100][100];
int pathmemo[100][100];
int n;
vector<vector<int>> triangle;
int trianglesum(int, int);
int main(){
    int c;
    cin >> c;
    for(int i=0; i<c; i++){
        cin >> n;
        memset(memo, 0, sizeof(memo));
        memset(pathmemo, -1, sizeof(pathmemo));
        for(int j=0 ;j<n; j++){
            int m;
            vector<int> v;
            triangle.push_back(v);
            for(int k=0; k<j+1 ;k++){
                cin >> m;
                triangle[j].push_back(m);
            }
            for(int k=0; k<n; k++){
                pathmemo[n-1][k] = 1;
            }            
        }
        triangle.clear();
        trianglesum(0, 0);
        cout << pathmemo[0][0] << "\n";
    }
}

int trianglesum(int x, int y){
    if(memo[x][y] != 0){
        return memo[x][y];
    }
    if(x == n-1){
        memo[x][y] = triangle[x][y];
        return memo[x][y];
    }
    memo[x][y] = triangle.at(x).at(y) + max(trianglesum(x+1, y), trianglesum(x+1, y+1));
    if(pathmemo[x][y]==-1){
        if(memo[x+1][y] == memo[x+1][y+1]){
            pathmemo[x][y] = pathmemo[x+1][y] + pathmemo[x+1][y+1];
        }
        else if(memo[x+1][y] > memo[x+1][y+1]){
            pathmemo[x][y] = pathmemo[x+1][y];
        }
        else{
            pathmemo[x][y] = pathmemo[x+1][y+1];
        }
    }
    return memo[x][y];
}