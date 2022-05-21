#include <iostream>
#include <string>
#include <vector>
#include <cstring>
#include <algorithm>

using namespace std;


struct ListNode {
    int val;
    ListNode *next;
    ListNode() : val(0), next(nullptr) {}
    ListNode(int x) : val(x), next(nullptr) {}
    ListNode(int x, ListNode *next) : val(x), next(next) {}
};
 
ListNode* addTwoNumbers(ListNode* l1, ListNode* l2) {
    ListNode* head = new ListNode();
    ListNode* node = head;
    int carry = 0;
    while(l1 != nullptr || l2 != nullptr){
        node -> next = new ListNode();
        node = node -> next;
        int sum = carry;
        if(l1 != nullptr){
            sum += l1 -> val;
        }
        if(l2 != nullptr){
            sum += l2 -> val;
        }
        if(sum > 9){
            carry = 1;
            sum %= 10;
        }
        else{
            carry = 0;
        }

        node -> val = sum;

        l1 = (l1 == nullptr) ? nullptr : l1->next;
        l2 = (l2 == nullptr) ? nullptr : l2->next;
    }

    if(carry != 0){
        node -> next = new ListNode(carry);
    }

    return head -> next;
};

int main(){
    ListNode a1(9);
    ListNode a2(9, &a1);
    ListNode a3(9, &a2);
    ListNode a4(9, &a3);
    ListNode a5(9, &a4);
    ListNode a6(9, &a5);
    ListNode a7(9);
    ListNode a8(9, &a7);
    ListNode a9(9, &a8);
    ListNode a10(9, &a9);

    // ListNode a1(2);
    // ListNode a2(4, &a1);
    // ListNode a3(3, &a2);
    // ListNode a7(5);
    // ListNode a8(6, &a7);
    // ListNode a9(4, &a8);
    

    ListNode* res = addTwoNumbers(&a6, &a10);
    while(res != nullptr){
        cout << res->val << endl;
        res = res->next;
    }
}