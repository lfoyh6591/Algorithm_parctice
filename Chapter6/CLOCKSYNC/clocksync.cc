#include <iostream>
#include <string>
#include <vector>

using namespace std;
int mincount;
vector<vector<int> > button({
    vector<int>( { 0, 1, 2 }),
    vector<int>( { 3, 7, 9, 11 }),
    vector<int>( { 4, 10, 14, 15 }),
    vector<int>( { 0, 4, 5, 6, 7 }),
    vector<int>( { 6, 7, 8, 10, 12 }),
    vector<int>( { 0, 2, 14, 15 }),
    vector<int>( { 3, 14, 15 }),
    vector<int>( { 4, 5, 7, 14, 15 }),
    vector<int>( { 1, 2, 3, 4, 5 }),
    vector<int>( { 3, 4, 5, 9, 13 })
});
void buttonnum(int[16], vector<vector<int>>, int, int);
int main(){
    int c;
    cin >> c;
    
    for(int i=0; i<c; i++){
        mincount = 5000;
        int clock[16];
        for(int j=0; j<16; j++){
            cin >> clock[j];
            clock[j] %=12;
            clock[j] /= 3;
        }
        buttonnum(clock, button, 0, 0);
        if(mincount>40){
            cout<<-1<<"\n";
        }
        else{
            cout<<mincount<<"\n";
        }
    }
}

void buttonnum(int clock[16], vector<vector<int>> button, int n, int count){    
    if(n>9){
        for(int i=0; i<16; i++){
            if(!(clock[i] == 0)){
                return;
            }
        }
        if(count<mincount){
            mincount = count;
        }
        return;
    }
    for(int i=0; i<4; i++){             
        buttonnum(clock, button, n+1, count+i);
        for(int j=0; j<button.at(n).size(); j++){                     
            clock[button[n][j]]++;
            clock[button[n][j]]%=4;                
        }           
    }    
}