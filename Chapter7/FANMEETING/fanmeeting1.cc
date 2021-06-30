#include <iostream>
#include <vector>
using namespace std;

int fanmeeting(bool*, bool*, int);
int main(){
    int c;
    cin >> c;
    for(int i=0; i<c; i++){
        string members;
        string fans;
        cin >> members;
        cin >> fans;
        vector<int> member;
        vector<int> fan;
        for(int j=0; j<members.length(); j++){
            member.push_back(members[j] == 'M');
        }
        for(int j=0; j<fans.length(); j++){
            fan[j] = (fans[j] == 'M');
        }        
    }
}
vector<int> add(vector<int> a, vector<int> b){//b is not shorter than a
    vector<int> result;
    int i;
    for(i=0; i<a.size(); i++){
        result.push_back(a[i]+b[i]);
    }
    for(; i<b.size(); i++){
        result.push_back(b[i]);
    }
    return result;
}
vector<int> sub(vector<int> a, vector<int> b){// a>=b
    vector<int> result;
    int i;
    for(i=0; i<b.size(); i++){
        result.push_back(a[i]-b[i]);
    }
    for(; i<a.size(); i++){
        result.push_back(a[i]);
    }
}
vector<int> multiply(vector<int> a, vector<int> b){
    vector<int> result(a.size() + b.size(), 0);
    for(int i=0; i<a.size(); i++){
        for(int j=0; j<b.size(); j++){
            result[i+j] += a[i]*b[j];
        }
    }
    return result;
}
vector<int> karatsuba(vector<int> a, vector<int> b){
    int alen = a.size();
    int blen = b.size();
    int ahalf = alen/2;
    int bhalf = blen/2;

    if(alen == 0 || blen == 0){
        return vector<int>();
    }

    if(blen<50){
        return multiply(a, b);
    }

    vector<int> a0(a.begin(), a.begin()+ahalf);
    vector<int> a1(a.begin()+ahalf, a.end());
    vector<int> b0(b.begin(), b.begin()+bhalf);
    vector<int> b1(b.begin()+bhalf, b.end());

    //implement karatsuba algorithm...
}
