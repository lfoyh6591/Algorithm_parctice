#include <iostream>
#include <string.h>
#include <algorithm>
#include <vector>
using namespace std;
double memo[50][50][101];
int n, d, p, t, q;
bool** graph;
double** graphper;
double percentage(int, int, int);
int main(){
    int C;
    cin >> C;    
    for(int c=0; c<C; c++){
        memset(memo, -1.0, sizeof(memo));
        cin >> n;
        cin >> d;
        cin >> p;
        graph = new bool*[n];
        graphper = new double*[n];
        for(int i=0; i<n; i++){
            graph[i] = new bool[n];
            graphper[i] = new double[n];
        }
        int k;
        for(int i=0; i<n; i++){
            int cnt = 0;
            for(int j=0; j<n; j++){
                cin >> k;
                if(k == 0){
                    graph[i][j] = false;
                }
                else{
                    graph[i][j] = true;
                    cnt ++;
                }
            }
            for(int j=0; j<n; j++){
                if(graph[i][j] && (cnt!=0)){
                    graphper[i][j] = (double)1/(double)(cnt);
                }
                else{
                    graphper[i][j] = 0;
                }
            }
        }
        cin >> t;
        cout << fixed;
        cout.precision(8);
        for(int i=0; i<t; i++){
            cin >> q;
            double result = percentage(p, q, d);
            cout << result << " ";
            //cout << percentage(p, q, d) << endl;
        }
        cout << "\n";
        delete graph;
        delete graphper;
    }
}

double percentage(int start, int end, int day){
    if(memo[start][end][day]>-0.5){
        return memo[start][end][day];
    }
    if(day == 1){
        memo[start][end][day] = graphper[start][end];
        return memo[start][end][day];
    }
    double& ret = memo[start][end][day];
    ret = 0.0;
    for(int i=0; i<n; i++){
        ret += graphper[start][i]*percentage(i, end, day-1);
    }
    //cout << "start " << start << " end " << end << " day " << day << " ret " << ret << endl;
    return ret;
}