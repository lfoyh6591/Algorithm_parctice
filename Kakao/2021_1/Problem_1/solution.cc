#include <string>
using namespace std;

string solution(string new_id) {
    for(auto it=new_id.begin(); it!=new_id.end(); it++){
        if(*it>=65 && *it<=90) *it+=32;
        if(!((*it>=48 && *it<=57) || (*it>=97 && *it<=122) || (*it==45) || (*it==46) || (*it==95))){
            new_id.erase(it--);
        }
    }
    bool beforeisdot = false;
    for(auto it=new_id.begin(); it!=new_id.end(); it++){
        if(*it=='.'){
            if(beforeisdot)  new_id.erase(it--);
            else             beforeisdot = true;
        }
        else{
            beforeisdot = false;
        }
    }

    if(new_id[0] == '.'){
        new_id.erase(new_id.begin());
    }
    else if(*(new_id.end()-1) == '.'){
        new_id.erase(new_id.end()-1);
    }

    if(new_id == "")    new_id = "a";

    if(new_id.size()>=16){
        for(auto it=new_id.begin()+15; it!=new_id.end();)   new_id.erase(it);
    }
    if(*(new_id.end()-1)=='.')  new_id.erase(new_id.end()-1);
    while(new_id.size()<=2){
        new_id+=*(new_id.end()-1);
    }
    return new_id;
}