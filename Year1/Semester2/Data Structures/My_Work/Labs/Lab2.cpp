#include <iostream>
using namespace std;

struct nod {
    int val;
    nod *next;
};

nod *head = nullptr;

void insert(const int val) {
    const auto ins = new nod();
    ins->val = val;
    if (head == nullptr) {
        ins->next = nullptr;
    } else {
        ins->next = head;
    }
    head = ins;
}

int pop() {
    if (head == nullptr) {
        return -1;
    }
    const nod *cop_head = head;
    const int cop_val = head->val;
    head = head->next;
    delete cop_head;
    return cop_val;
}

struct nodD {
    int val;
    nodD *next, *prev;
};

nodD *headD = nullptr;
nodD *tailD = nullptr;

void insertD(const int val) {
    const auto ins = new nodD();
    ins->val = val;
    ins->prev = nullptr;
    if (headD == nullptr) {
        ins->next = nullptr;
        tailD = ins;
    } else {
        ins->next = headD;
        headD->prev = ins;
    }
    headD = ins;
}

int popD() {
    if ( tailD == nullptr) {
        return -1;
    }
    const int pop_val = tailD->val;
    const nodD *cop_tailD = tailD;
    tailD = tailD->prev;
    if (tailD != nullptr) {
        tailD->next = nullptr;
    }
    delete cop_tailD;
    return pop_val;
}


int main() {
    insertD(5);
    insertD(4);
    insertD(1);
    insertD(2);
    insertD(3);

    cout << popD() << endl;
    cout << popD() << endl;
    cout << popD() << endl;
    cout << popD() << endl;
    cout << popD() << endl;

    return 0;
}
