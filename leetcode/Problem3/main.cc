#include <iostream>
#include <string>
#include <vector>
#include <string.h>
#include <cstring>
#include <algorithm>

using namespace std;

/*int lengthOfLongestSubstring(string s) {
    int k=0;
    vector<int> res;
    int max_res = 0;
    int state = 0;
    int start = 0;
    for(int i=0; i<s.size(); i++){
        for(int j=0; j<res.size(); j++){
            if(s[res[j]] == s[i]){
                state = 1;
                i=res[j];
                if(res.size()>=max_res){
                    max_res = res.size();
                }
                res.clear();
                break;
            }
        }
        if(state == 0){
            res.push_back(i);
        }
        else{
            state = 0;
        }
    }
    if(res.size()>=max_res){
        max_res = res.size();
    }
    cout << "max_res " << max_res << endl;
    return max_res;
}*/

int lengthOfLongestSubstring(string s) {
    vector<int> v(128, -1);
    int left = 0;
    int right = 1;
    int max_len = 0;
    while(right <= s.size()){
        char c = s[right-1];

        int index = v[c];
        if(index!=-1 && (index>=left && index<right)){
            max_len = max(max_len, right - left-1);
            left = index + 1;
        }

        v[c] = right-1;

        right++;
    }
    max_len = max(max_len, right - left-1);
    return max_len;
}

int main(){
    cout << lengthOfLongestSubstring("abcabcbb") << endl;
}