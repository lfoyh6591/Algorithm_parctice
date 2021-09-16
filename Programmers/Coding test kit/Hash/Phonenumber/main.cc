#include <string>
#include <vector>

using namespace std;

bool checkvector(vector<string> v){
    vector<vector<string>> newv(10);
    if(v.size()<=1){
        return true;
    }
    else{
        for(int i=0; i<v.size(); i++){
            if(v[i]==""){
                return false;
            }
            else{
                int hashnum = int(v[i][0])-48;
                newv[hashnum].push_back(v[i].substr(1));
                //cout << "hashnum " << hashnum << " " << v[i].substr(1) << endl;
            }
        }
    }
    for(int i=0; i<10; i++){
        if(!checkvector(newv[i])){
            return false;
            break;
        }
    }
    return true;
}

bool solution(vector<string> phone_book) {
    bool answer = true;
    answer = checkvector(phone_book);
    return answer;
}