#include <bits/stdc++.h>
using namespace std;
struct treenode{
    int p, q;
    treenode* left;
    treenode* right;
};
int n;
int cnt;

treenode* deleteRoot(treenode* t){
    if((t->left == NULL) && (t->right == NULL)){
        t = NULL;
    }
    else if(t->left == NULL){
        t = t->right;
    }
    else if(t->right == NULL){
        t = t->left;
    }
    else{
        treenode* &temp = t->right;
        while(temp->left!=NULL){
            temp = temp->left;
        }
        t->p = temp->p;
        t->q = temp->q;
        temp = deleteRoot(temp);
    }
    return t;
}

treenode* maketreenode(int p1, int q1, treenode* t){
    if(t == NULL){
        t = new treenode;
        t->p = p1;
        t->q = q1;
        t->left = NULL;
        t->right = NULL;
        cnt++;
    }
    else{
        if((t->p > p1) && (t->q > q1)){
            return t;
        }
        else if((t->p < p1) && (t->q < q1)){
            t = deleteRoot(t);
            cnt--;
            maketreenode(p1, q1, t);
        }
        else if((t->p < p1) && (t->q > q1)){
            t->right = maketreenode(p1, q1, t->right);
  
        }
        else if((t->p > p1) && (t->q < q1)){
            t->left = maketreenode(p1, q1, t->left);
        }
    }
    return t;
}

int main(){    
    int C;    cin >> C;
    for(int c=0; c<C; c++){
        cin >> n;
        cnt = 0;
        int sum = 0;
        treenode* nerd = NULL;
        for(int i=0; i<n; i++){
            int p, q;
            cin >> p >> q;
            nerd = maketreenode(p, q, nerd);
            sum += cnt;
        }
        cout << sum << endl;
    }
}