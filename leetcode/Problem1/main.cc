#include <iostream>
#include <string>
#include <vector>
#include <cstring>
#include <algorithm>

using namespace std;

vector<int> twoSum(vector<int>& nums, int target) {

    vector<int> a;
    int i=0;
    int j=nums.size()-1;
    vector<int> temp;

    for(int k=0; k<nums.size(); k++){
        temp.push_back(nums[k]);
    }

    sort(nums.begin(), nums.end());
    
    while(true){
        if((nums[i]+nums[j])==target){
            break;
        }
        else if((nums[i]+nums[j])>target){
            j--;
        }
        else{
            i++;
        }
    }

    for(int k=0; k<nums.size(); k++){
        if((temp[k] == nums[i])||(temp[k] == nums[j])){
            a.push_back(k);
        }
    }
    
    return a;

};

int main(){
    vector<int> num;
    num = {5, 3, 2, 8};
    vector<int> v = twoSum(num, 10);
}