#include <iostream>
#include <string.h>
#include <algorithm>
#include <vector>
#include <queue>
#include <map>
using namespace std;
int n;
vector<int> list;

int bfs(){
    vector<int> sorted = list;
    sort(sorted.begin(), sorted.end());
    if(sorted == list)  return 0;

    queue<vector<int>> q;
    map<vector<int>, int> distance;
    q.push(list);
    distance[list] = 0;

    while(!q.empty()){
        vector<int> v = q.front();
        q.pop();
        int distancev = distance[v];

        for(int i=0; i<n-1; i++){
            for(int j=i+2; j<n+1; j++){
                reverse(v.begin()+i, v.begin()+j);
                if(distance[v]==0){
                    if(v==sorted){
                        return distancev+1;
                    }
                    distance[v] = distancev+1;
                    q.push(v);
                }
                reverse(v.begin()+i, v.begin()+j);
            }
        }
    }
    return 0;
}

int main(){
    int C;    cin >> C;
    for(int c=0; c<C; c++){
        cin >> n;
        list.clear();
        for(int i=0; i<n; i++){
            int k;  cin >> k;
            list.push_back(k);
        }

        cout << bfs() << endl;
    }
}