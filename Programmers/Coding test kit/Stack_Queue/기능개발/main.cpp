#include <string>
#include <vector>
#include <queue>

using namespace std;

vector<int> caldays(vector<int> progresses, vector<int> speeds){
    vector<int> days(progresses.size());
    for(int i=0; i<progresses.size(); i++){
        if((100-progresses[i])%speeds[i]==0){
            days[i] = (100-progresses[i])/speeds[i];
        }
        else{
            days[i] = (100-progresses[i])/speeds[i] + 1;
        }
    }
    return days;
}

vector<int> solution(vector<int> progresses, vector<int> speeds) {
    vector<int> answer;
    vector<int> days = caldays(progresses, speeds);
    queue<int> q;
    int cnt = 0;
    for(int i=0; i<days.size(); i++){
        if(q.empty()||(q.front()>=days[i])){
            q.push(days[i]);
        }
        else{
            answer.push_back(q.size());
            queue<int> empty;
            swap(q, empty);
            q.push(days[i]);
        }
    }
    answer.push_back(q.size());
    return answer;
}