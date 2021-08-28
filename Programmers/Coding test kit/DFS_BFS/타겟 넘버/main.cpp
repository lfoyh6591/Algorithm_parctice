#include <string>
#include <vector>
#include <queue>

using namespace std;

int solution(vector<int> numbers, int target) {
    int answer = 0;
    queue<int> q;
    q.push(numbers[0]);
    q.push(-numbers[0]);
    int rank = 1;   int cnt = 0;    int t = 2;
    while(!q.empty()){
        int sum = q.front();    q.pop();
        
        q.push(sum+numbers[rank]);
        q.push(sum-numbers[rank]);
        cnt++;
        if(cnt == t){
            rank++;
            cnt = 0;
            t*=2;
        }
        if(rank==numbers.size()){
            while(!q.empty()){
                if(q.front()==target){
                    answer++;
                    q.pop();
                }
                else{
                    q.pop();
                }
            }
        }
    }
    
    return answer;
}