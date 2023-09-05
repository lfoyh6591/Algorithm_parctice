#include <iostream>
#include <string>
#include <vector>
#include <cstring>

using namespace std;
int compression(string s, int n);

int solution(string s) {
    int length = s.length();
    int answer = length;
    for(int i=1; i<length/2+1; i++){
        int temp = compression(s, i);
        if(answer > temp){
            answer = temp;
        }
    }
    return answer;
}

int compression(string s, int n){
    int l = s.length();
    int min = s.length();
    int temp = l;
    string standard;
    int number = 0;
    for(int j=0; j<s.length(); j+=n){
        string now = s.substr(j, n);
        if(j == 0){
            standard = now;
            continue;
        }
        if(!strcmp(standard.c_str(), now.c_str())){
            if(number == 0){
                temp -= n-1;
                number++;
            }
            else{
                temp -= n;
                number++;
                if(number == 9){
                    temp += 1;
                }
                else if(number == 99){
                    temp += 1; 
                }
                else if(number == 999){
                    temp += 1;
                }
            }
        }
        else{
            standard = now.substr(0, n);
            number = 0;
        }
    }
    if(min > temp){
        min = temp;
    }
    return min;
}

int main(){
    cout << solution("aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa") << endl;
}