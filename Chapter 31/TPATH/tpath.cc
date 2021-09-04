#include <bits/stdc++.h>
using namespace std;
int n, m;
vector<map<int, vector<int>>> graph;

int prim(){
    priority_queue<pair<int, tuple<int, pair<int, int>, vector<bool>>>> pq;
    vector<bool> check(n, false);
    check[0] = true;
    for(auto it=graph[0].begin(); it!=graph[0].end(); it++){
        int there = it->first;
        for(int j=0; j<graph[0][there].size(); j++){
            pq.push(make_pair(0, make_tuple(there, make_pair(graph[0][there][j], graph[0][there][j]), check)));
        }
    }

    while(!pq.empty()){
        int gap = -pq.top().first;
        int here = get<0>(pq.top().second);
        if(here==n-1){
            return gap;
        }
        int mintime = get<1>(pq.top().second).first;
        int maxtime = get<1>(pq.top().second).second;
        vector<bool> check1 = get<2>(pq.top().second);
        pq.pop();

        for(auto it=graph[here].begin(); it!=graph[here].end(); it++){
            int there = it->first;
            cout << "there " << there << endl;
            if(!check1[there]){
                check1[there] = true;
                for(int j=0; j<it->second.size(); j++){
                    int cost = graph[here][there][j];

                    if(cost<mintime){
                        pq.push(make_pair(-(maxtime-cost), make_tuple(there, make_pair(cost, maxtime), check1)));
                    }
                    else if(cost>maxtime){
                        pq.push(make_pair(-(cost-mintime), make_tuple(there, make_pair(mintime, cost), check1)));
                    }
                    else{
                        pq.push(make_pair(-gap, make_tuple(there, make_pair(mintime, maxtime), check1)));
                    }
                }
                check1[there] = false;
            }
        }
        check1.clear();
    }
    return 0;
}

int main(){
    int C;    cin >> C;
    for(int c=0; c<C; c++){
        cin >> n >> m;
        graph.clear();
        graph.resize(n);
        for(int i=0; i<m; i++){
            int x, y, z;    cin >> x >> y >> z;
            graph[x][y].push_back(z);
            graph[y][x].push_back(z);
        }
        cout << prim() << endl;
    }
}