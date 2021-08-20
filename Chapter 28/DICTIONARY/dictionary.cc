#include <iostream>
#include <string.h>
#include <algorithm>
#include <vector>
using namespace std;
int n;
int state;
string input[1000];
vector<char> seq;
vector<char>::iterator it;
bool check[26];

int findindex(char s){
    for(int i=0; i<seq.size(); i++){
        if(seq[i] == s){
            return i;
        }
    }
    return 0;
}

vector<char>::iterator findit(char s){
    for(it = seq.begin(); it!=seq.end(); it++){
        if(*it == s){
            return it;
        }
    }
    return seq.begin();
}

void findseq(){
    for(int i=0; i<n-1; i++){
        int al = input[i].size();
        int bl = input[i+1].size();

        for(int j=0; j<min(al, bl); j++){
            char c1 = input[i][j];
            char c2 = input[i+1][j];
            if(c1 == c2){
                if(j==min(al, bl)-1){
                    if(al>bl){
                        state = 1;
                        return;
                    }
                }
                continue;
            }
            else{
            if(check[c1-'a'] && check[c2-'a']){
                if(findindex(c1)>findindex(c2)){
                    state = 1;
                    return;
                }
            }
            else if(check[c1-'a'] && !check[c2-'a']){
                /*it = findit(c1);
                seq.insert(it+1, c2);*/
                seq.push_back(c2);
                check[c2-'a'] = true;
            }
            else if(!check[c1-'a'] && check[c2-'a']){
                it = findit(c2);
                seq.insert(it, c1);
                check[c1-'a'] = true;
            }
            else if(!check[c1-'a'] && !check[c2-'a']){
                seq.push_back(c1);
                seq.push_back(c2);
                check[c1-'a'] = true;
                check[c2-'a'] = true;
            }
            break;
            }
        }
    }
}

void print(){
    if(state == 1){
        cout << "INVALID HYPOTHESIS" << endl;
        return;
    }
    else{
        for(it=seq.begin(); it!=seq.end(); it++){
            cout << *it;
        }
        for(int i=0; i<26; i++){
            if(!check[i]){
                cout << (char)(i+'a');
            }
        }
        cout << endl;
    }
    return;
}

int main(){
    int C;    cin >> C;
    for(int c=0; c<C; c++){
        cin >> n;
        memset(check, false, sizeof(check));
        for(int i=0; i<n; i++){
            cin >> input[i];
        }
        state = 0;
        findseq();
        print();
        seq.clear();
    }
}