#include <bits/stdc++.h>
using namespace std;
#define INF 987654321

int V, E, s, t;
vector<int> delay;
vector<vector<int>> original;
vector<vector<int>> graph;
vector<vector<int>> via;

void floyd(){
    via.clear();    via.resize(V);
    for(int i=0; i<V; i++){
        via[i].resize(V, -1);
    }
    for(int i=0; i<V; i++){
        graph[i][i] = 0;
        original[i][i] = 0;
    }
    for(int k=0; k<V; k++){
        for(int i=0; i<V; i++){
            for(int j=0; j<V; j++){
                if(graph[i][j] > graph[i][k] + graph[k][j]){
                    graph[i][j] = graph[i][k] + graph[k][j];
                    via[i][j]=k;
                }
            }
        }
    }
}

int findBigdelay(int u, int v, int through){ 
    if(through == -1){
        int ret = max(delay[u], delay[v]);
        return ret;
    }

    int ret = max(delay[u], delay[v]);
    ret = max(ret, delay[through]);
    ret = max(ret, findBigdelay(u, through, via[u][through]));
    ret = max(ret, findBigdelay(through, v, via[through][v]));

    return ret;
}

int plusDelay(){ 
    if(s==t)    return 0;
    int ret = INF;
    for(int i=0; i<V; i++){
        int bigdelay = findBigdelay(s, t, i);
        int sibigdelay = findBigdelay(s, i, via[s][i]);
        int itbigdelay = findBigdelay(i, t, via[i][t]);

        //cout << "s " << s << " t " << t << " i " << i << " bigdelay " << bigdelay << " sibigdelay " << sibigdelay << " itbigdelay " << itbigdelay << endl; 

        if(sibigdelay == 0) sibigdelay = INF;
        if(itbigdelay == 0) itbigdelay = INF;

        //ret = min(ret, original[s][i] + original[i][t] + delay[i]);
        ret = min(ret, graph[s][i] + sibigdelay + original[i][t]);
        ret = min(ret, original[s][i] + graph[i][t] + itbigdelay);
        ret = min(ret, graph[s][i] + graph[i][t] + bigdelay);
    }
    return ret;
}

int main(){
    cin >> V >> E;

    delay.resize(V);
    for(int i=0; i<V; i++){
        cin >> delay[i];
    }

    graph.resize(V);    original.resize(V);
    for(int i=0; i<V; i++){
        graph[i].resize(V); original[i].resize(V);
        for(int j=0; j<V; j++){
            graph[i][j] = INF;
            original[i][j] = INF;
        }
    }

    for(int i=0; i<E; i++){
        int a, b, c;
        cin >> a >> b >> c;
        graph[a-1][b-1] = c;
        graph[b-1][a-1] = c;
        original[a-1][b-1] = c;
        original[b-1][a-1] = c;
    }

    floyd();

    int T;    cin >> T;
    for(int i=0; i<T; i++){
        cin >> s >> t;
        s--;    t--;
        int delays = delay[s];
        int delayt = delay[t];
        delay[s] = 0;
        delay[t] = 0;
        cout << plusDelay() << endl;
        delay[s] = delays;
        delay[t] = delayt;
    }
    //cout << findBigdelay(2, 4, via[2][4]) << "aa" << via[2][4] <<  endl;
}