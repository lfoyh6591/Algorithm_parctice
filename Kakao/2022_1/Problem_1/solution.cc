#include <string>
#include <vector>
#include <map>
#include <cstring>

using namespace std;

vector<int> solution(vector<string> id_list, vector<string> report, int k) {
    map<string, int> m;
    vector<int> v(id_list.size(), 0);
    vector<int> mail(id_list.size(), 0);
    bool check[1000][1000];
    memset(check, false, sizeof(check));

    for(int i=0; i<id_list.size(); i++){
        m[id_list[i]] = i;
    }

    for(int i=0; i<report.size(); i++){
        string a, b;
        for(int j=0; j<report[i].size(); j++){
            if(report[i][j] == ' '){
                a = report[i].substr(0, j);
                b = report[i].substr(j+1);
                break;
            }
        }
        int a_id = m[a];
        int b_id = m[b];
        if(check[a_id][b_id])   continue;
        else{
            check[a_id][b_id] = true;
            v[b_id]++;
        }
    }

    for(int i=0; i<v.size(); i++){
        if(v[i]>=k){
            for(int j=0; j<v.size(); j++){
                if(check[j][i]){
                    mail[j]++;
                }
            }
        }
    }

    return mail;
}