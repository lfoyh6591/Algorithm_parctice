#include <iostream>
#include <string.h>
#include <algorithm>
#include <vector>
using namespace std;
int n, p, l;
long long memolength[50];
string memodragon[50][2];
string dragon(int, int, int);
string setdragon(int, int);
long long dragonlength(int);
int main(){
    int C;
    cin >> C;
    memset(memolength, -1, sizeof(memolength));
    for(int i=0; i<50; i++){
        memodragon[i][0] = "";
        memodragon[i][1] = "";
    }
    for(int c=0; c<C; c++){
        cin >> n;
        cin >> p;
        cin >> l;
        long long length = dragonlength(n);
        cout << dragon(n, p, l) << endl;
        //cout << dragonlength(41) << endl;
    }
}

string dragon(int generation, int p, int l){
    if(generation == 0){
        return setdragon(0, 0).substr(p-1, l);

    }
    string ret;
    if(p+l-1 <= dragonlength(generation-1)){
        for(int i=generation-1; i>=0; i--){
            if(p+l-1 > dragonlength(i)){
                generation = i+2;
                break;
            }
        }
        ret = setdragon(generation, 0).substr(p-1, l);
    }
    if(p> dragonlength(generation-1)){
        if(p == dragonlength(generation-1)+1){

            ret = "+" + setdragon(5, 1).substr(0, l-1);
        }
        else{
            for(int i=generation-1; i>=0; i--){
                if(p <= dragonlength(i)){
                    generation = i+2;
                    break;
                }
            }
            ret = setdragon(generation, 1).substr(p-dragonlength(generation-1)-1, l);
        }
    }
    else if(p<=dragonlength(generation-1) && p+l-1>dragonlength(generation-1)){
        string first = dragon(generation, p, dragonlength(generation-1)-p+1);
        string last = dragon(generation, dragonlength(generation-1)+1, l-(dragonlength(generation-1)-p+1));
        ret = first + last;
    }
    return ret;
}

string setdragon(int generation, int state){ // 0 is front, 1 is back
    if(generation == 0){
        memodragon[0][0] = "FX";
        return "FX";
    }
    if(generation == 1){
        if(state == 0){
            memodragon[1][0] = "FX";
            return "FX";
        }
        if(state == 1){
            memodragon[1][1] = "YF";
            return "YF";
        }
    }
    if(memodragon[generation][state] != ""){
        return memodragon[generation][state];
    }

    string& ret = memodragon[generation][state];
    string s = setdragon(generation-1, state);
    for(int i=0; i<s.size(); i++){
        if(s.at(i) == 'X'){
            ret += "X+YF";
        }
        else if(s.at(i) == 'Y'){
            ret += "FX-Y";
        }
        else{
            ret += s.substr(i, 1);
        }
    }
    return ret;
}

long long dragonlength(int generation){
    if(generation == 0){
        memolength[0] = 2;
        return 2;
    }
    if(memolength[generation]!=-1){
        return memolength[generation];
    }

    long long& ret = memolength[generation];
    ret = 2*dragonlength(generation-1) + 1;
    return ret;
}