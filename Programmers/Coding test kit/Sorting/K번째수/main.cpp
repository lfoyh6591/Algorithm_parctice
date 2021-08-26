#include <string>
#include <vector>
#include <algorithm>

using namespace std;

vector<int> solution(vector<int> array, vector<vector<int>> commands) {
    vector<int> answer;
    for(int i=0; i<commands.size(); i++){
        int ii = commands[i][0];
        int jj = commands[i][1];
        int kk = commands[i][2];
        vector<int> copyvector(jj-ii+1);

        copy(array.begin()+ii-1, array.begin()+jj, copyvector.begin());
        sort(copyvector.begin(), copyvector.end());
        
        answer.push_back(copyvector[kk-1]);
    }
    return answer;
}