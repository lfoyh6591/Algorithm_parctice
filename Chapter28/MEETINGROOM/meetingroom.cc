#include <iostream>
#include <string.h>
#include <algorithm>
#include <vector>
#include <stack>
using namespace std;
int n;
int id, idnum[400];
vector<pair<int, int>> meeting;
vector<vector<int>> graph;
vector<vector<int>> scc;
stack<int> s;
bool dfscheck[400];
bool stackcheck[400];
bool scccheck[400];

bool isoverlap(pair<int, int> a, pair<int, int> b){
    if(a.first <= b.first){
        if(a.second>b.first){
            return true;
        }
    }
    else{
        if(b.second>a.first){
            return true;
        }
    }
    return false;
}
void makegraph(){
    int size = meeting.size();
    graph.clear();  graph.resize(2*size);

    for(int i=0; i<size; i+=2){ // same team
        int j = i+1;  // i -> week, j -> month
        graph[2*i].push_back(2*j+1); // i => !j
        graph[2*i+1].push_back(2*j); // !i => j
        graph[2*j].push_back(2*i+1); // j => !i
        graph[2*j+1].push_back(2*i); // !j => i
    }

    for(int i=0; i<size; i++){
        for(int j=0; j<i; j++){
            if(isoverlap(meeting[i], meeting[j])){
                graph[2*i].push_back(2*j+1);
                graph[2*j].push_back(2*i+1);
            }
        }
    }
}
int makescc(int here){
    idnum[here] = id++;
    int parent = idnum[here];
    dfscheck[here] = true;
    //stackcheck[here] = true;
    s.push(here);

    for(int i=0; i<graph[here].size(); i++){
        int j = graph[here][i];
        if(!dfscheck[j]){
            parent = min(parent, makescc(j));
        }
        else if(!scccheck[j]){
            parent = min(parent, idnum[j]);
        }
    }

    if(parent == idnum[here]){
        vector<int> newscc;
        while(true){
            int k = s.top();
            newscc.push_back(k);
            scccheck[k] = true;
            stackcheck[k] = false;
            s.pop();
            cout << "k " << k << endl;
            if(k == here)  break;
        }
        scc.push_back(newscc);
    }
    return parent;
}

int main(){
    int C;    cin >> C;
    for(int c=0; c<C; c++){
        cin >> n;
        scc.clear();
        memset(dfscheck, false, sizeof(dfscheck));
        memset(scccheck, false, sizeof(scccheck));
        memset(stackcheck, false, sizeof(stackcheck));
        memset(idnum, 0, sizeof(idnum));
        id = 0;
        for(int i=0; i<n; i++){
            int a, b, c, d;
            cin >> a >> b >> c >> d;
            pair<int, int> week = make_pair(a, b);    
            pair<int, int> month = make_pair(c, d);
            meeting.push_back(week);
            meeting.push_back(month);
        }

        makegraph();

        for(int i=0; i<graph.size(); i++){
            if(!scccheck[i]){
                makescc(i);
            }
        }
        /*
        for(int i=0; i<graph.size(); i++){
            for(int j=0; j<graph[i].size(); j++){
                cout << " i " << i << " graph[i][j] " << graph[i][j] << endl;
            }
        }*/

        for(int i=0; i<scc.size(); i++){
            cout << "scc " << i << " start ";
            for(int j=0; j<scc[i].size(); j++){
                cout << scc[i][j] << " ";
            }
            cout << endl;
        }


    }
}