#include <iostream>
#include <vector>
#include <string>
using namespace std;
string quadtree(string);
int main(){
    int c = 0;
    cin >> c;
    for(int i=0; i<c; i++){
        string s;
        cin >> s;
        string result = quadtree(s);
        cout << result << "\n";
    }
}

string quadtree(string s){
    if(s.size() == 1){
        return s;
    }
    string part[4];
    int index = 0;
    for(int i=1; i<s.size(); i++){
        if(s[i] == 'x'){
            part[index++] = quadtree(s.substr(i));
            i+=part[index-1].size()-1;
        }
        else{
            part[index++] = s[i];
        }
        if(index>3){
            break;
        }
    }
    return "x"+part[2]+part[3]+part[0]+part[1];
}

