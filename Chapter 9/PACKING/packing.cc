#include <iostream>
#include <string.h>
#include <algorithm>
#include <vector>
using namespace std;
int memo[1001][101];
int n, bagw;
int want[100], weight[100];
string name[100];
vector<string> items;
void unpacking(int, int);
int packing(int, int);
int main(){
    int C;
    cin >> C;    
    for(int c=0; c<C; c++){
        memset(memo, -1, sizeof(memo));
        cin >> n;
        cin >> bagw;
        for(int i=0; i<n; i++){
            string s;
            cin >> s;
            name[i] = s;
            int x;
            cin >> x;
            weight[i] = x;
            cin >> x;
            want[i] = x;
        }
        int result = packing(bagw, 0);
        unpacking(bagw, 0);
        cout << packing(bagw, 0) << " " << items.size() << endl;
        int x = items.size();
        for(int i=0; i<x; i++){
            string s = items.back();
            items.pop_back();
            cout << s << endl;
        }
        
    }
}

int packing(int w, int item){
    if(memo[w][item] != -1){
        return memo[w][item];
    }
    if(item == n){
        memo[w][n] == 0;
        return 0;
    }
    int& ret = memo[w][item];
    ret = packing(w, item+1);
    
    if(w>=weight[item]){
        ret = max(ret, packing(w-weight[item], item+1) + want[item]);
    }
    return ret;
}

/*
void unpacking(){
    int k = bagw;
    for(int i=0; i<n; i++){
        if(k-weight[i]>=0){
            if(packing(k,i) == packing(k-weight[i],i+1) + want[i]){
                items.push_back(name[i]);
                k -= weight[i];
            }
        }
    }
}*/
void unpacking(int w, int item){
    if(item == n){
        return;
    }
    if(packing(w, item) == packing(w, item+1)){
        unpacking(w, item+1);
    }
    else{
        items.push_back(name[item]);
        unpacking(w-weight[item], item+1);
    }
}