#include <bits/stdc++.h>
using namespace std;
int n, k, m, l;
vector<vector<int>> classes;
vector<vector<int>> term;
int memo[10][1<<12];

vector<vector<int>> selectClass(vector<int> v, vector<int> result, vector<bool> check, vector<vector<int>>& ret){
    if(result.size()==l){
        ret.push_back(result);
        return ret;
    }

    for(int i=0; i<v.size(); i++){
        if(!check[i]){
            for(int j=0; j<i+1; j++){
                check[j]=true;
            }
            result.push_back(v[i]);
            ret = selectClass(v, result, check, ret);
            for(int j=0; j<i+1; j++){
                check[j]=false;
            }
            result.pop_back();
        }
    }
    return ret;
}

vector<int> availbleClass(int semester, int state){
    vector<int> v;
    for(int i=0; i<term[semester].size(); i++){
        int cnt = 0;
        if((state&(1<<term[semester][i])) == 0){
            for(int j=0; j<classes[term[semester][i]].size(); j++){
                if(state&(1<<classes[term[semester][i]][j])){
                    cnt++;
                }
                else    break;
            }
            if(cnt == classes[term[semester][i]].size()){
                v.push_back(term[semester][i]);
            }
        }
    }
    return v;
}

int takeClass(int semester, int state){
    if(__builtin_popcount(state) >= k){
        return 0;
    }
    else if(semester >= m){
        return 987654321;
    }

    if(memo[semester][state]!=-1){
        return memo[semester][state];
    }

    vector<int> v = availbleClass(semester, state);
    if(v.size()==0){
        memo[semester][state] = takeClass(semester+1, state);
    }
    else if(v.size()<=l){
        int newstate = state;
        for(int i=0; i<v.size(); i++){
            newstate |= (1<<v[i]);
        }
        memo[semester][state] = min(takeClass(semester+1, state), takeClass(semester+1, newstate)+1);
    }
    else{
        vector<bool> check(v.size(), false);
        vector<int> result;
        vector<vector<int>> selected;
        selected = selectClass(v, result, check, selected);
        memo[semester][state] = takeClass(semester+1, state);

        for(int i=0; i<selected.size(); i++){
            int newstate = state;
            for(int j=0; j<l; j++){
                newstate |= (1<<selected[i][j]);
            }
            memo[semester][state] = min(takeClass(semester+1, newstate)+1, memo[semester][state]);
        }
    }
    return memo[semester][state];
}

int main(){    
    int C;    cin >> C;
    for(int c=0; c<C; c++){
        cin >> n >> k >> m >> l;
        memset(memo, -1, sizeof(memo));
        classes.resize(n);  term.resize(m);
        for(int i=0; i<n; i++){
            int r;    cin >> r;
            for(int j=0; j<r; j++){
                int cl; cin >> cl;
                classes[i].push_back(cl);
            }
        }
        for(int i=0; i<m; i++){
            int r;      cin >> r;
            for(int j=0; j<r; j++){
                int cl; cin >> cl;
                term[i].push_back(cl);
            }
        }
        int result = takeClass(0, 0);
        if(result>m){
            cout << "IMPOSSIBLE" << endl;
        }
        else{
            cout << result << endl;
        }
        classes.clear();    term.clear();
    }
}