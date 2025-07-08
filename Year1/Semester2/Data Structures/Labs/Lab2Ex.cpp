#include <iostream>

using namespace std;

struct ListNode {
    int val;
    ListNode *next;

    ListNode() : val(0), next(nullptr) {
    }

    explicit ListNode(const int x) : val(x), next(nullptr) {
    }

    ListNode(const int x, ListNode *next) : val(x), next(next) {
    }
};

ListNode *head = nullptr;

void insert(const int val) {
    auto *ins = new ListNode(val);
    if (head == nullptr) {
        head = ins;
    } else {
        ListNode *temp = head;
        while (temp->next != nullptr) {
            temp = temp->next;
        }
        temp->next = ins;
    }
}

int pop() {
    if (head == nullptr) {
        return -1;
    }
    const ListNode *cop_head = head;
    const int cop_val = head->val;
    head = head->next;
    delete cop_head;
    return cop_val;
}

ListNode *insertionSortList(ListNode *head) {
    if (head == nullptr || head->next == nullptr) return head;

    ListNode *sorted = nullptr;
    ListNode *curr = head;

    while (curr) {
        ListNode *next = curr->next;

        if (!sorted || sorted->val >= curr->val) {
            curr->next = sorted;
            sorted = curr;
        } else {
            ListNode *temp = sorted;
            while (temp->next && temp->next->val < curr->val) {
                temp = temp->next;
            }
            curr->next = temp->next;
            temp->next = curr;
        }
        curr = next;
    }

    return sorted;
}


int main() {
    insert(4);
    insert(2);
    insert(7);
    insert(8);
    insert(1);
    insert(3);
    insert(5);
    insert(6);

    head = insertionSortList(head);

    cout << "Sorted List: ";
    while (head) {
        cout << pop() << " ";
    }
    cout << endl;

    return 0;
}
