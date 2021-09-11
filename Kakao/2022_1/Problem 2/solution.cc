#include <iostream>
#include <string>
#include <vector>
#include <cmath>

using namespace std;

string translate(int n, int k){
    string trans = "";
    double cnt = 0;
    while(n!=0){
        trans = to_string(n%k) + trans;
        n/=k;
    }
    return trans;
}

bool isprime(long long n){
    if(n<2){
        return false;
    }
    for(int i=2; i<=(int)sqrt(n); i++){
        if(n%i == 0){
            return false;
        }
    }
    return true;
}

int solution(int n, int k) {
    int answer = 0;
    string trans = translate(n, k);
    int prev = 0;
    for(int i=0; i<trans.size(); i++){
        if(trans[i] == '0'){
            if(i==prev){
                prev = i+1;
                continue;
            }
            if(isprime(stoll(trans.substr(prev, i-prev)))){
                cout << trans.substr(prev, i-prev) << endl;
                answer++;
            }
            prev = i+1;
        }
    }
    if(prev<trans.size() && isprime(stoll(trans.substr(prev, trans.size()-prev)))){
        cout << trans.substr(prev, prev-trans.size()) << endl;
        answer++;
    }

    return answer;
}

int main(){
    int c;
    cin >> c;
    for(int i=0; i<c ; i++){
    int n, k;
    cin >> n >> k;
    cout << translate(n, k) << endl;
    cout << solution(n, k) << endl;
    }
}