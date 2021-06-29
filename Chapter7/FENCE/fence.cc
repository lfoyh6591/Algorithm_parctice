#include <iostream>
using namespace std;
int cutting(int*, int, int);
int main(){
    int c;
    cin >> c;
    for(int i=0; i<c; i++){
        int n;
        cin >> n;
        int *fence = new int[n];
        for(int j=0; j<n; j++){
            cin >> fence[j];
        }
        cout << cutting(fence, 0, n) << "\n";
    }
}

int cutting(int *fence, int left, int right){
    if((right-left)==1){
        return fence[left];
    }
    int mid = (left+right-1)/2;
    int result = max(cutting(fence, left, mid+1), cutting(fence, mid+1, right));
    int minheight = min(fence[mid], fence[mid+1]);
    int rec = 2*minheight;
    int index1= mid;
    int index2 = mid+1;
    while(index1!=left || index2!=right-1){
        if(index1==left){
            minheight = min(minheight, fence[++index2]);
            rec = max(rec, minheight*(index2-index1+1));
        }
        else if(index2==right-1){
            minheight = min(minheight, fence[--index1]);
            rec = max(rec, minheight*(index2-index1+1));
        }
        else{
            if(fence[index1-1]>fence[index2+1]){
                index1--;
                minheight = min(minheight, fence[index1]);
                rec = max(rec, minheight*(index2-index1+1));
            }
            else{
                index2++;
                minheight = min(minheight, fence[index2]);
                rec = max(rec, minheight*(index2-index1+1));
            }
        }
    }
    return max(result, rec);
}