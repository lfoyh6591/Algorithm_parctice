#include <string>
#include <vector>
#include <map>
#include <iostream>

using namespace std;

vector<int> solution(vector<string> info, vector<string> query) {
    vector<int> answer;
    map<int, vector<int>> m; //score, info
    for(int i=0; i<info.size(); i++){
        int infonum = 0;
        int blank = 0;
        bool meetblank = true;
        string score;
        for(auto it=info[i].begin(); it!=info[i].end(); it++){
            if(meetblank){
                meetblank = false;
                if(blank == 0){
                    if(*it == 'c'){
                        infonum = 0;
                        it+=2;
                    }
                    else if(*it == 'j'){
                        infonum = 1;
                        it+=3;
                    }
                    else if(*it == 'p'){
                        infonum = 2;
                        it+=5;
                    }
                }
                if(blank == 1){
                    if(*it == 'f'){
                        infonum += (1<<2);
                    }
                    it+=6;
                }
                else if(blank == 2){
                    if(*it == 's'){
                        infonum += (1<<3);
                    }
                    it+=5;
                }
                else if(blank == 3){
                    if(*it == 'p'){
                        infonum += (1<<4);
                        it+=4;
                    }
                    else{
                        it+=6;
                    }
                }
                else if(blank == 4){
                    while(it!=info[i].end()){
                        score+=*it;
                        it++;
                    }
                    m[stoi(score)].push_back(infonum);
                    break;
                }
            }
            if(*it==' '){
                blank++;
                meetblank = true;
            }
        }
    }
    
    for(int i=0; i<query.size(); i++){
        int infonum=0;
        int notcare=0;
        int cnt=0;
        int blank = 0;
        bool meetblank = true;
        string score;
        for(auto it=query[i].begin(); it!=query[i].end(); it++){
            if(meetblank){
                meetblank = false;
                if(blank == 0){
                    if(*it == 'c'){
                        infonum =0;
                        it+=2;
                    }
                    else if(*it == 'j'){
                        infonum = 1;
                        it+=3;
                    }
                    else if(*it == 'p'){
                        infonum = 2;
                        it+=5;
                    }
                    else if(*it == '-'){
                        notcare = 3;
                    }
                }
                if(blank == 2){
                    if(*it == 'f'){
                        infonum += (1<<2);
                        it+=6;
                    }
                    else if(*it == '-'){
                        notcare += (1<<2);
                    }
                    else{
                        it+=6;
                    }
                }
                else if(blank == 4){
                    if(*it == 's'){
                        infonum += (1<<3);
                        it+=5;
                    }
                    else if(*it == '-'){
                        notcare += (1<<3);
                    }
                    else{
                        it+=5;
                    }
                }
                else if(blank == 6){
                    if(*it == 'p'){
                        infonum += (1<<4);
                        it+=4;
                    }
                    else if(*it == '-'){
                        notcare += (1<<4);
                    }
                    else{
                        it+=6;
                    }
                }
                else if(blank == 7){
                    while(it!=query[i].end()){
                        score+=*it;
                        it++;
                    }
                    auto itt = m.lower_bound(stoi(score));
                    for( ; itt!=m.end(); itt++){
                        for(int i=0; i<itt->second.size(); i++){
                            int n = itt->second[i];
                            n^=infonum;
                            n = 31-n;
                            n|=notcare;
                            if(n==31){
                                cnt++;
                            }
                        }
                    }
                    answer.push_back(cnt);
                    break;
                }/*
                else{
                    it+=2;
                }*/
            }
            if(*it==' '){
                blank++;
                meetblank = true;
            }
        }
    }
    return answer;
}
/*
int main(){
    vector<string> info, query;
    info.push_back("java backend junior pizza 150");
    info.push_back("python frontend senior chicken 210");
    info.push_back("python frontend senior chicken 150");
    info.push_back("cpp backend senior pizza 260");
    info.push_back("java backend junior chicken 80");
    info.push_back("python backend senior chicken 50");

    query.push_back("java and backend and junior and pizza 100");
    query.push_back("python and frontend and senior and chicken 200");
    query.push_back("cpp and - and senior and pizza 250");
    query.push_back("- and backend and senior and - 150");
    query.push_back("- and - and - and chicken 100");
    query.push_back("- and - and - and - 150");
    vector<int> v = solution(info, query);
    for(int i=0; i<v.size(); i++){
        cout << v[i] << endl;
    }
}*/