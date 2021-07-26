#include <iostream>
#include <string.h>
#include <algorithm>
#include <vector>
using namespace std;
int n, k;
int num[500];
int minnum = 0;
vector<int> list;
double memolength[501];
double memocnt[501];
double lislength(int);
double liscount(int);
int main(){
    int C;
    cin >> C;
    
    for(int c=0; c<C; c++){
        memset(memolength, -1, sizeof(memolength));
        memset(memocnt, -1, sizeof(memocnt));
        cin >> n;
        cin >> k;
        for(int i=0; i<n; i++){
            cin >> num[i];
        }
        double lis = 0;
        for(int i=0; i<n; i++){
            lis = max(lis, lislength(i));
        }
        cout << lis << endl;
        for(int i=0; i<n; i++){
            double b = liscount(i);
        }
        /*for(int i=0; i<n; i++){
            cout << "memolength " << memolength[i] << " memocount " << memocnt[i] << endl;
        } for debugging */ 
        int index = 0;
        int minv = 987654321;
        while(lis>0){
        for(int i=0; i<n; i++){
            if((memolength[i] == lis) && num[i] > minnum){
                minv = min(minv, num[i]);
                index = i;
            }
        }
        minnum = minv;
        if(memocnt[index]<k){
            k -= memocnt[index];
        }
        else{
            if(list.empty() || list.back() < num[index]){
                list.push_back(num[index]);
                lis--;
                minv = 987654321;
            }
        }
        }
        for(int i=0; i<list.size(); i++){
            cout << list.at(i) << " ";
        }
        cout << endl;
        list.clear();
        minnum = 0;
    }
}

double lislength(int start){
    if(start == n){
        return 0;
    }
    if(memolength[start] >= -0.5){
        return memolength[start];
    }
    double& ret = memolength[start];
    ret = 1;
    for(int i=start+1; i<n; i++){
        if(num[start]<num[i]){
            ret = max(ret, lislength(i)+1);
        }
    }
    return ret;
}

double liscount(int start){
    if(memolength[start] <= 1){
        memocnt[start] = 1;
    }
    if(memocnt[start] >= -0.5){
        return memocnt[start];
    }
    double&ret = memocnt[start];
    ret = 0;
    for(int i=start+1; i<n; i++){
        if((memolength[i] == memolength[start]-1) && (num[start] < num[i])){
            ret+=liscount(i);
        }
    }
    return ret;
}