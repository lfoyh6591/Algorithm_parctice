#include <string>
#include <vector>
#include <map>
using namespace std;

vector<int> solution(vector<int> fees, vector<string> records) {
    vector<int> answer;
    map<string, int> totaltime;
    map<string, string> inandout;
    
    for(int i=0; i<records.size(); i++){
        string time = records[i].substr(0, 5);
        string id = records[i].substr(6, 4);
        string inout = records[i].substr(11, 2);

        if(inout == "IN"){
            inandout[id] = time;
        }
        else{
            string intime = inandout[id];
            int minutes = (stoi(time.substr(0, 2))-stoi(intime.substr(0, 2)))*60 + stoi(time.substr(3, 2)) - stoi(intime.substr(3, 2));
            if(totaltime.find(id)!=totaltime.end()){
                totaltime[id]+=minutes;
            }
            else{
                totaltime[id] = minutes;
            }
            inandout.erase(id);
        }
    }

    for(auto it=inandout.begin(); it!=inandout.end(); it++){
        string id = it->first;
        string intime = it->second;
        int minutes = (23-stoi(intime.substr(0, 2)))*60 + 59 - stoi(intime.substr(3, 2));
        if(totaltime.find(id)!=totaltime.end()){
            totaltime[id]+=minutes;
        }
        else{
            totaltime[id] = minutes;
        }    
    }

    for(auto it=totaltime.begin(); it!=totaltime.end(); it++){
        int t = it->second;
        if(t<=fees[0]){
            answer.push_back(fees[1]);
        }
        else{
            int totalfee = fees[1];
            t-=fees[0];
            totalfee += (t/fees[2])*fees[3];
            if(t%fees[2] != 0)  totalfee+=fees[3];
            answer.push_back(totalfee);
        }
    }

    return answer;
}