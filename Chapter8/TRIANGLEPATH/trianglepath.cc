#include <iostream>
#include <vector>
#include <string.h>
using namespace std;
int memo[100][100];
int n;
int trianglesum(int, int, vector<vector<int>>);
int main(){
    int c;
    cin >> c;
    for(int i=0; i<c; i++){
        cin >> n;
        memset(memo, 0, sizeof(memo));
        vector<vector<int>> triangle;
        for(int j=0 ;j<n; j++){
            int m;
            vector<int> v;
            triangle.push_back(v);
            for(int k=0; k<j+1 ;k++){
                cin >> m;
                triangle[j].push_back(m);
            }            
        }
        cout << trianglesum(0, 0, triangle) << "\n";
    }
}

int trianglesum(int x, int y, vector<vector<int>> triangle){
    if(memo[x][y] != 0){
        return memo[x][y];
    }
    if(x == n-1){
        memo[x][y] = triangle[x][y];
        return memo[x][y];
    }
    memo[x][y] = triangle.at(x).at(y) + max(trianglesum(x+1, y, triangle), trianglesum(x+1, y+1, triangle));
    return memo[x][y];
}