#include <string>
#include <vector>
#include <map>

using namespace std;

string solution(vector<string> participant, vector<string> completion) {
    string answer = "";
    map<string, int> m;
    for(int i=0; i<participant.size(); i++){
        if(m.find(participant[i])==m.end()){
            m.insert(make_pair(participant[i], 1));
        }
        else{
            m[participant[i]]++;
        }
    }
    for(int i=0; i<completion.size(); i++){
        if(m[completion[i]]==1){
            m.erase(completion[i]);
        }
        else{
            m[completion[i]]--;
        }
    }
    auto it = m.begin();
    answer = it->first;
    return answer;
}