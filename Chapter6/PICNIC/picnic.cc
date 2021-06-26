#include<iostream>
#include<string>
#include<vector>
using namespace std;
int findmatching(vector<pair<int, int>>, int, int, bool[], int);
int main(){
    int testcase;
    cin >> testcase;

    for(int i=0; i<testcase; i++){
        int n, m;
        cin >> n;
        cin >> m;
        vector<pair<int, int>> friends;
        for(int j=0; j<m; j++){
            int a, b;
            cin >> a;
            cin >> b;
            friends.push_back(make_pair(a, b));
        }
        int result = 0;
        for(int j=0; j<m-(n/2)+1; j++){
            bool *check = new bool[n];
            for(int k=0; k<n; k++){
                check[k] = false;
            }
            result += findmatching(friends, n, j, check, 0);
        }
        cout << result << "\n";
    }
}

int findmatching(vector<pair<int, int>> friends, int n, int vectorindex, bool check[], int matchednum){
    if(vectorindex > friends.size()-1){
        return 0;
    }    
    if(check[friends.at(vectorindex).first] || check[friends.at(vectorindex).second]){
        return 0;
    }
    if(matchednum+2 == n){
        return 1;
    }
    int result = 0;

    check[friends.at(vectorindex).first] = true;
    check[friends.at(vectorindex).second] = true;

    for(int i=vectorindex+1; i<friends.size(); i++){
        result+=findmatching(friends, n, i, check, matchednum+2);
    }

    check[friends.at(vectorindex).first] = false;
    check[friends.at(vectorindex).second] = false;

    return result;
}