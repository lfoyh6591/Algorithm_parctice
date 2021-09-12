#include <iostream>
#include <string>
#include <vector>

using namespace std;
vector<int> lion(11, 0);
vector<int> app;
vector<int> result(11, 0);
int maxnum = 0;

int process(int n, int k){
    if(n == 0){
        int lionscore = 0;
        int appscore = 0;
        for(int i=0; i<lion.size(); i++){
            if(lion[i]>app[i]){
                lionscore+=10-i;
            }
            else{
                if(app[i] == 0) continue;
                appscore+=10-i;
            }
        }
        return lionscore-=appscore;        
    }
    else{
        for(int i=k; i<lion.size(); i++){
            if(lion[i]<=app[i]){
                if(n<app[i]+1)  continue;
                lion[i] = app[i]+1;
                int res = process(n-app[i]-1, i+1);
                if(maxnum < res){
                    maxnum = res;
                    for(int i=10; i>=0; i--){
                        cout << " i " << i << endl;
                        if((result[i] == 0) && (lion[i] == 0))  continue;
                        if(result[i] == lion[i])    continue;
                        if(lion[i] > result[i]){
                            result = lion;
                            break;
                        }
                    }
                }
                lion[i] = 0;
            }
        }
    }
    return 0;
}

vector<int> solution(int n, vector<int> info) {
    app = info;
    process(n, 0);
    bool updated = true;
    for(int i=0; i<result.size(); i++){
        if(result[i] == 0){
            continue;
        }
        else{
            updated = false;
            break;
        }
    }
    if(updated){
        vector<int> v(1, -1);
        return v;
    }
    return result;
}

int main(){
    vector<int> info;
    info.push_back(2);
    info.push_back(1);
    info.push_back(1);
    info.push_back(1);
    info.push_back(0);
    info.push_back(0);
    info.push_back(0);
    info.push_back(0);
    info.push_back(0);
    info.push_back(0);
    info.push_back(0);
    vector<int> v = solution(5, info);
    for(int i=0; i<v.size(); i++){
        cout << v[i] << endl;
    }
}
