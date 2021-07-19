#include <iostream>
#include <string.h>
#include <algorithm>
#include <vector>
using namespace std;
string word[500];
int sentence[100];
double memo[101][501];
double T[500][500];
double M[500][500];
double B[500];
vector<string> original;
int n, m;
double ocr(int, int);
void reconstruct(int);
int main(){
    memset(memo, -1.0, sizeof(memo));
    int q;
    cin >> m;    
    cin >> q;
    for(int i=0; i<m; i++){
       cin >> word[i];
    }
    for(int i=0; i<m; i++){
        cin >> B[i];
    }
    for(int i=0; i<m; i++){
        for(int j=0; j<m; j++){
            cin >> T[i][j];
        }
    }
    for(int i=0; i<m; i++){
        for(int j=0; j<m; j++){
            cin >> M[i][j];
        }
    }
    for(int i=0; i<q; i++){
        memset(memo, -1.0, sizeof(memo));
        cin >> n;
        for(int j=0; j<n; j++){
            string s;
            cin >> s;
            for(int k=0; k<m; k++){
                if(word[k] == s){
                    sentence[j] = k;
                    break;
                }
            }
        }
        double prob = 0.0;
        for(int j=0; j<m; j++){
            prob = max(prob, ocr(n-1, j));
        }
        reconstruct(n-1);
        for(int j=0; j<original.size(); j++){
            cout << original.back() << " ";
            original.pop_back();
        }
        cout << endl;
    }
}

double ocr(int index, int word){
    if(index == 0){
        memo[0][word] = B[word];
        return memo[0][word];
    }
    if(memo[index][word]>-0.5){
        return memo[index][word];
    }
    double& ret = memo[index][word];
    for(int i=0; i<m; i++){
        ret = max(ret, M[sentence[word]][word]*T[i][word]*ocr(index-1, i));
    }
    return ret;
}

void reconstruct(int last){
    double maxp = 0.0;
    int x=0;
    for(int i=0; i<m; i++){
        maxp = max(maxp, memo[last][i]);
        x = i;
    }
    original.push_back(word[x]);
    for(int i=last; i>0; i--){
        for(int j=0; j<m; j++){
            if(ocr(i, j) == M[sentence[x]][x]*T[j][x]*ocr(i-1, j)){
                x = j;
                original.push_back(word[x]);
                continue;
            }
        }
    }
}