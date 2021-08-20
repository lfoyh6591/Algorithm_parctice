#include <iostream>
using namespace std;
int membernum;
int fannum;
int fanmeeting(bool*, bool*, int);
int main(){
    int c;
    cin >> c;
    for(int i=0; i<c; i++){
        string member;
        string fan;
        cin >> member;
        cin >> fan;

        bool *checkmalemember = new bool[member.length()];
        bool *checkmalefan = new bool[fan.length()];
        membernum = member.length();
        fannum = fan.length();
        for(int j=0; j<membernum; j++){
            if(member[j] == 'M'){
                checkmalemember[j] = true;
            }
            else{
                checkmalemember[j] = false;
            }
        }

        for(int j=0; j<fannum; j++){
            if(fan[j] == 'M'){
                checkmalefan[j] = true;
            }
            else{
                checkmalefan[j] = false;
            }
        }
        cout << fanmeeting(checkmalemember, checkmalefan, 0) << "\n";
    }
}

int fanmeeting(bool* member, bool* fan, int index){
    if((index+membernum)>fannum){
        return 0;
    }
    for(int i=index; i<index+membernum; i++){
        if(member[i-index] && fan[i]){
            int a=0;
            int b=0;
            while(member[i-index] && (i-index)<membernum){
                a++;
                i++;
            }
            i-=a;
            while(fan[i] && i<fannum){
                b++;
                i++;
            }
            return fanmeeting(member, fan, index+max(a, b));
        }
    }
    return fanmeeting(member, fan, index+1)+1;
}