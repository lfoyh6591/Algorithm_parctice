#include <iostream>
#include <string>
using namespace std;
int h, w;
int dx1[4] = {0, 0, 1, 1};
int dy1[4] = {1, 1, 0, 0};
int dx2[4] = {1, 1, 1, 1};
int dy2[4] = {1, 0, -1, 1};
int findmatching(bool**);
bool checkfigure(bool**, int, int, int);
void changefigure(bool**&, int, int, int);
int main(){
    int c;
    cin >> c;
    for(int i=0; i<c; i++){
        h, w;
        cin >> h;
        cin >> w;
        cin.ignore();
        bool **board = new bool*[h];
        for(int j=0; j<h; j++){
            board[j] = new bool[w];
        }
        int white = 0;
        for(int j=0; j<h; j++){
            string s;
            getline(cin, s);
            for(int k=0; k<w; k++){
                if(s.at(k) == '#'){
                    board[j][k] = true;
                }
                else{
                    board[j][k] = false;
                    white++;
                }
            }
        }
        int result = 0;
        if(white%3 != 0){}
        else{
            result = findmatching(board);        
        }
        cout << result << "\n";
    }
}

int findmatching(bool** board){
    int result = 0;
    int x, y;
    x = -1;
    y = -1;
    for(int i=0; i<h; i++){
        int a = 0;
        for(int j=0; j<w; j++){
            if(!board[i][j]){
                x = i;
                y = j;
                a = 1;
                break;
            }
        }
        if(a == 1){
            break;
        }
    }

    if((x == -1) && (y == -1)){
        return 1;
    }
    bool state[4];
    for(int i=0; i<4; i++){
        if(!checkfigure(board, x, y, i)){
            state[i] = false;
        }
        else{
            state[i] = true;
            changefigure(board, x, y, i);
            result += findmatching(board);
            changefigure(board, x, y, i);
        }
    }
    int check = 0;
    for(int i=0; i<4; i++){
        if(!state[i]){
            check++;
        }
    }
    if(check == 4){
        return 0;
    }
    return result;
}

bool checkfigure(bool** board, int x, int y, int state){
    int x1 = x+dx1[state];
    int y1 = y+dy1[state];
    int x2 = x+dx2[state];
    int y2 = y+dy2[state];
    if((x1<0) || (x1>h-1) || (y1<0) || (y1>w-1) || (x2<0) || (x2>h-1) || (y2<0) || (y2>w-1)){
        return false;
    }
    if(board[x1][y1] || board[x2][y2]){
        return false;
    }
    return true;
}

void changefigure(bool** &board, int x, int y, int state){
    int x1 = x+dx1[state];
    int y1 = y+dy1[state];
    int x2 = x+dx2[state];
    int y2 = y+dy2[state];
    board[x][y] = !board[x][y];
    board[x1][y1] = !board[x1][y1];
    board[x2][y2] = !board[x2][y2];
}