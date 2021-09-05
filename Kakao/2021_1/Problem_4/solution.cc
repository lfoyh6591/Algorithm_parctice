#include <string>
#include <vector>
#include <queue>
#include <iostream>
#define INF 987654321
using namespace std;

int solution(int n, int s, int a, int b, vector<vector<int>> fares) {
    vector<vector<pair<int, int>>> graph(n+1);

    for(int i=0; i<fares.size(); i++){
        graph[fares[i][0]].push_back(make_pair(fares[i][1], fares[i][2]));
        graph[fares[i][1]].push_back(make_pair(fares[i][0], fares[i][2]));
    }

    vector<vector<int>> dist(n+1, vector<int>(n+1, INF));

    priority_queue<pair<int, pair<int, int>>, vector<pair<int, pair<int, int>>>, greater<pair<int, pair<int, int>>>> pq;
    dist[s][s] = 0;
    pq.push(make_pair(0, make_pair(s, s)));

    while(!pq.empty()){
        int ahere = pq.top().second.first;
        int bhere = pq.top().second.second;
        int d = pq.top().first;
        pq.pop();

        if(d>dist[ahere][bhere])    continue;
        if(ahere==a && bhere==b){
            continue;
        }
        else if(ahere == a){
            for(int i=0; i<graph[bhere].size(); i++){
                int there = graph[bhere][i].first;
                int cost = graph[bhere][i].second;
                if(dist[a][there] > d+cost){
                    dist[a][there] = d+cost;
                    pq.push(make_pair(d+cost, make_pair(a, there)));
                }
            }
        }
        else if(bhere == b){
            for(int i=0; i<graph[ahere].size(); i++){
                int there = graph[ahere][i].first;
                int cost = graph[ahere][i].second;
                if(dist[there][b] > d+cost){
                    dist[there][b] = d+cost;
                    pq.push(make_pair(d+cost, make_pair(there, b)));
                }
            }
        }
        else{   
            for(int i=0; i<graph[ahere].size(); i++){
                int athere = graph[ahere][i].first;
                int acost = graph[ahere][i].second;
                for(int j=0; j<graph[bhere].size(); j++){
                    int bthere = graph[bhere][j].first;
                    int bcost = graph[bhere][j].second;
                    if((ahere == bhere) && (athere == bthere)){
                        if(dist[athere][bthere] > d+acost){
                            dist[athere][bthere] = d+acost;
                            pq.push(make_pair(d+acost, make_pair(athere, bthere)));
                        }
                    }
                    else{
                        if(dist[athere][bthere] > d+acost+bcost){
                            dist[athere][bthere] = d+acost+bcost;
                            pq.push(make_pair(d+acost+bcost, make_pair(athere, bthere)));
                        }   
                    }
                }
            }
        }
    }
    return dist[a][b];
}
/*
int main(){
    int n = 6;  int s = 4;  int a = 6;  int b = 2;
    vector<vector<int>> v;
        vector<int> v1;
        v1.push_back(4);
        v1.push_back(1);
        v1.push_back(10);
        v.push_back(v1);
        v1.clear();
        v1.push_back(3);
        v1.push_back(5);
        v1.push_back(24);
        v.push_back(v1);
        v1.clear();
        v1.push_back(5);
        v1.push_back(6);
        v1.push_back(2);
        v.push_back(v1);
        v1.clear();
        v1.push_back(3);
        v1.push_back(1);
        v1.push_back(41);
        v.push_back(v1);
        v1.clear();
        v1.push_back(5);
        v1.push_back(1);
        v1.push_back(24);
        v.push_back(v1);
        v1.clear();
        v1.push_back(4);
        v1.push_back(6);
        v1.push_back(50);
        v.push_back(v1);
        v1.clear();
        v1.push_back(2);
        v1.push_back(4);
        v1.push_back(66);
        v.push_back(v1);
        v1.clear();
        v1.push_back(2);
        v1.push_back(3);
        v1.push_back(22);
        v.push_back(v1);
        v1.clear();
        v1.push_back(1);
        v1.push_back(6);
        v1.push_back(25);
        v.push_back(v1);
        cout << solution(n, s, a, b, v) << endl;
}*/