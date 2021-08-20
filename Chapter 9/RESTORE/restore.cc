#include <iostream>
#include <string.h>
#include <algorithm>
#include <vector>
using namespace std;
string input[15];
vector<int> sequence;
int overlap[15][15];
bool check[15];
int k;
int ret;
void overlapcal();
int restore(int, int);
int overlapsize(string, string);
int main(){
    int C;
    cin >> C;
    for(int c=0; c<C; c++){
        cin >> k;
        memset(overlap,-1, sizeof(overlap));
        for(int i=0; i<k; i++){
            cin >> input[i];
            check[i] = false;
        }
        overlapcal();
        int length = 0;
        ret = 0;
        int value = 0;
        for(int i=0; i<k; i++){
            value = max(restore(i, 1), value);
        }
        cout << value << endl;
    }
}

int restore(int last, int length){
    if(length == k){
        return ret;
    }
    int ret = 0;
    for(int i=0; i<k; i++){
        if(check[i]){
            continue;
        }
        check[i] = true;
        ret = max(ret, overlap[last][i]+restore(i, length+1));
        check[i] = false;
    }
    return ret;
}

void overlapcal(){
    for(int i=0; i<k; i++){
        for(int j=0; j<k; j++){
            if(i==j){
                continue;
            }
            overlap[i][j] = overlapsize(input[i], input[j]);
        }
    }
}

int overlapsize(string a, string b){
    int al = a.size();
    int bl = b.size();
    int ret = 0;
    for(int i=0; i<al; i++){
        if(al-i>=bl){
            if(a.substr(i, bl) == b.substr(0)){
                ret = max(ret, bl);
            }
        }
        else{
            if(a.substr(i) == b.substr(0, al-i)){
                ret = max(ret, al-i);
            }
        }
    }
    return ret;
}