#include <iostream>
#include <string>
#include <vector>
#include <queue>

using namespace std;
vector<pair<int, pair<int, int>>> v(17);
vector<bool> check(17, false);

void maketree(vector<int> info, vector<vector<int>> edges){
    int n = info.size();
    for(int i=0; i<n; i++){
        v[i].first = -1;
        v[i].second.first = -1;
        v[i].second.second = -1;
    }

    for(int i=0; i<edges.size(); i++){
        int p = edges[i][0];
        int c = edges[i][1];

        v[c].first = p;
        if(v[p].second.first == -1){
            v[p].second.first = c;
        }
        else{
            v[p].second.second = c;
        }
    }
}

int process(vector<int> info, int sheep, int wolf, int node){
    if(node == -1)  return sheep;

    int lchild = v[node].second.first;
    int rchild = v[node].second.second;
    check[node] = true;

    if(!info[node]){
        sheep++;

    }
    else{
        wolf++;
    }

}

int solution(vector<int> info, vector<vector<int>> edges) {
    int answer = 0;
    int n = info.size();
    vector<bool> check(n, false);
    maketree(info, edges);
    int sheep = 0;
    int wolf = 0;

    queue<int> q;
    q.push(0);  sheep = 1;
    int sheepinq=1;

    while(true){
        int here = q.front();
        q.pop();
        if(here == -1)  continue;
        int lchild = v[here].second.first;
        int rchild = v[here].second.second;
        int parent = v[here].first;

        if(!info[here]){
            sheep++;
            sheepinq--;
            check[here] = true;
            if(lchild!=-1){
                q.push(lchild);
                if(!info[lchild])   sheepinq++;
            }
            if(rchild!=-1){
                q.push(rchild);
                if(!info[rchild])    sheepinq++;
            }
        }
        else{
            if(sheepinq!=0){
                q.push(here);
            }
            else{
                if(lchild==-1 && rchild==-1){
                    continue;
                }
                else{
                    
                }
            }
        }
    }
    

    return answer;
}

// int main(){
//     vector<int> info;
//     vector<vector<int>> edges;

//     info.push_back(0);
//     info.push_back(0);
//     info.push_back(1);
//     info.push_back(1);
//     info.push_back(1);
//     info.push_back(0);
//     info.push_back(1);
//     info.push_back(0);
//     info.push_back(1);
//     info.push_back(0);
//     info.push_back(1);
//     info.push_back(1);

//     vector<int> v(2);
//     v[0] = 0;
//     v[1] = 1;
//     edges.push_back(v);
//     v[0] = 1;
//     v[1] = 2;
//     edges.push_back(v);
//     v[0] = 1;
//     v[1] = 4;
//     edges.push_back(v);
//     v[0] = 0;
//     v[1] = 8;
//     edges.push_back(v);
//     v[0] = 8;
//     v[1] = 7;
//     edges.push_back(v);
//     v[0] = 9;
//     v[1] = 10;
//     edges.push_back(v);
//     v[0] = 9;
//     v[1] = 11;
//     edges.push_back(v);
//     v[0] = 4;
//     v[1] = 3;
//     edges.push_back(v);
//     v[0] = 6;
//     v[1] = 5;
//     edges.push_back(v);
//     v[0] = 4;
//     v[1] = 6;
//     edges.push_back(v);
//     v[0] = 8;
//     v[1] = 9;
//     edges.push_back(v);

//     cout << solution(info, edges) << endl;
// }