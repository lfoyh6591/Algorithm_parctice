#include <iostream>
#include <string.h>
#include <algorithm>
using namespace std;
int memo[10001];
int n;
string input;
int difficulty(string);
int diffsum(int);
bool diff1(string);
bool diff2(string);
bool diff4(string);
bool diff5(string);
int main(){
    int C;
    cin >> C;    
    for(int c=0; c<C; c++){
        memset(memo, 0, sizeof(memo));
        cin >> input;
        cout<<diffsum(0) << "\n";
    }
}
int diffsum(int begin){
    if(memo[begin]!=0){
        return memo[begin];
    }
    if(input.size()-begin<3){
        memo[begin] = 987654321;
        return 987654321;
    }
    if((input.size()-begin>=3) && (input.size()-begin<=5)){
        memo[begin] = difficulty(input.substr(begin));
        return memo[begin];
    }
    memo[begin] = min({(difficulty(input.substr(begin, 3))+diffsum(begin+3)), (difficulty(input.substr(begin, 4))+diffsum(begin+4)), (difficulty(input.substr(begin, 5))+diffsum(begin+5))});
    return memo[begin];
}
int difficulty(string num){
    if(diff1(num)){
        return 1;
    }
    else if(diff2(num)){
        return 2;
    }
    else if(diff4(num)){
        return 4;
    }
    else if(diff5(num)){
        return 5;
    }
    else{
        return 10;
    }
}
bool diff1(string num){
    for(int i=0; i<num.size()-1; i++){
        if(num[i]!=num[i+1]){
            return false;
        }
    }
    return true;
}
bool diff2(string num){
    if(num[1]-num[0] == 1){
        for(int i=1; i<num.size()-1; i++){
            if(num[i+1]-num[i]!=1){
                return false;
            }
        }
        return true;
    }
    else if(num[1]-num[0] == -1){
        for(int i=1; i<num.size()-1; i++){
            if(num[i+1]-num[i]!=-1){
                return false;
            }
        }
        return true;
    }
    return false;
}
bool diff4(string num){
    if(num.size()==3){
        if(num[0] == num[2]){
            return true;
        }
        return false;
    }
    else if(num.size()==4){
        if(num[0] == num[2]){
            if(num[1] == num[3]){
                return true;
            }
        }
        return false;
    }
    else if(num.size()==5){
        if(num[0] == num[2]){
            if(num[1] == num[3]){
                if(num[2] == num[4]){
                    return true;
                }
            }
        }
        return false;
    }
    return false;
}
bool diff5(string num){
    for(int i=0; i<num.size()-2; i++){
        if((num[i+1] - num[i])!=(num[i+2] - num[i+1])){
            return false;
        }
    }
    return true;
}