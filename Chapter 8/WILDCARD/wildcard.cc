#include <iostream>
#include <algorithm>
#include <vector>
#include <string>
using namespace std;
int comparestring(string, string);

int main(){
    int c;
    cin >> c;
    for(int i=0; i<c; i++){
        string w;
        cin >> w;
        int n;
        cin >> n;
        vector<string> file;
        for(int j=0; j<n; j++){
            string s;
            cin >> s;
            if(comparestring(w, s)>0){
                file.push_back(s);
            }
        }
        sort(file.begin(), file.end());
        for(int j=0; j<file.size(); j++){
            cout << file[j] << "\n";
        }
    }
}

int comparestring(string w, string file){
    if(file.size()==0){
        if((w.size()==1) && w[0]=='*'){
            return 1;
        }
        else { return 0;}
    }    
    if(w.size() == 1){
        if(w[0] == file[0]){
            if(file.size() == 1){
                return 1;
            }
            else { return 0;}
        }
        else if(w[0] == '?'){
            if(file.size()==1){
                return 1;
            }
            else {return 0;}
        }
        else if(w[0] == '*'){
            return 1;
        }
        return 0;
    }

    if((w[0]!='?') && (w[0]!='*')){
        if(w[0]==file[0]){
            if(w.size()==1 && file.size()==1){
                return 1;
            }
            else{
                return comparestring(w.substr(1), file.substr(1));
            }
        }
        else{ return 0; }
    }
    else if(w[0] == '?'){
        return comparestring(w.substr(1), file.substr(1));
    }
    else if(w[0] == '*'){
        int maxv = 0;
        for(int i=0; i<file.size(); i++){
            maxv = max(maxv, comparestring(w.substr(1), file.substr(i)));
        }
        return maxv;
    }
    return 0;
}