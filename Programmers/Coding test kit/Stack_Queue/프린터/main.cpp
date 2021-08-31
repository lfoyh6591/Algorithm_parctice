#include <string>
#include <vector>
#include <queue>
#include <algorithm>
#include <string.h>
using namespace std;

int solution(vector<int> priorities, int location) {
    int answer = 0;
    int importancenum[10];
    int maxi = 0;
    
    memset(importancenum, 0, sizeof(importancenum));
    
    for(int i=0; i<priorities.size(); i++){
        maxi = max(maxi, priorities[i]);
        importancenum[priorities[i]]++;
    }
    int vsize = priorities.size();
    
    while(vsize!=0){
        if(priorities[0] == maxi){
            if(location == 0){
                return answer+1;
            }
            importancenum[maxi]--;
            if(importancenum[maxi] == 0){
                for(int i=maxi; i>0; i--){
                    if(importancenum[i]!=0){
                        maxi = i;
                        break;
                    }
                }
            }
            priorities.erase(priorities.begin());
            vsize--;
            answer++;
            location--;
        }
        else{
            if(location == 0){
                location = vsize-1;
            }
            else{
                location--;
            }
            priorities.push_back(priorities[0]);
            priorities.erase(priorities.begin());
        }
    }
    return answer;
}