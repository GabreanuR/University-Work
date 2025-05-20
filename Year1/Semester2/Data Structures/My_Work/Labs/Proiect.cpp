//Binomial Heap - Găbreanu Răzvan-George

//Sources:
//https://www.youtube.com/watch?v=UqvGHUNd9Uw&list=PLv9sD0fPjvSHqIOLTIvHJWjkdH0IdzmXT&index=21
//https://www.youtube.com/watch?v=FtMzl6cmjkc&list=PLv9sD0fPjvSHqIOLTIvHJWjkdH0IdzmXT&index=22
//https://www.youtube.com/watch?v=-82Wd64fxtw&list=PLv9sD0fPjvSHqIOLTIvHJWjkdH0IdzmXT&index=23
//https://www.youtube.com/watch?v=ZN2Z2EITFC4&list=PLv9sD0fPjvSHqIOLTIvHJWjkdH0IdzmXT&index=24

#include <iostream>
using namespace std;

struct Node {
    Node *parent;
    int key;
    int degree;
    Node *leftmostChild;
    Node *immediateRightSibling;

    explicit Node(const int value) {
        this->key = value;
        this->degree = 0;
        this->parent = nullptr;
        this->leftmostChild = nullptr;
        this->immediateRightSibling = nullptr;
    }
};

class BinomialHeap {
    Node *head;

public:
    BinomialHeap() {
        head = nullptr;
    }

    [[nodiscard]] Node *getHead() const {
        return head;
    }

    Node *setHead(Node *node) {
        head = node;
        return head;
    }

    //Step 1: Merge 2 linked lists of roots
    static Node *mergeRootLists(Node *L1, Node *L2) {
        if (L1 == nullptr) return L2;
        if (L2 == nullptr) return L1;

        Node *head = nullptr;
        Node *tail = nullptr;

        if (L1->degree <= L2->degree) {
            head = tail = L1;
            L1 = L1->immediateRightSibling;
        } else {
            head = tail = L2;
            L2 = L2->immediateRightSibling;
        }

        while (L1 != nullptr && L2 != nullptr) {
            if (L1->degree <= L2->degree) {
                tail->immediateRightSibling = L1;
                L1 = L1->immediateRightSibling;
            } else {
                tail->immediateRightSibling = L2;
                L2 = L2->immediateRightSibling;
            }
            tail = tail->immediateRightSibling;
        }

        if (L1 != nullptr) tail->immediateRightSibling = L1;
        else tail->immediateRightSibling = L2;

        return head;
    }

    //Step 2: Combine binomial trees of same order
    static void linkTrees(Node *T1, Node *T2) {
        T1->parent = T2;
        T1->immediateRightSibling = T2->leftmostChild;
        T2->leftmostChild = T1;
        T2->degree++;
    }

    static Node *unionHeap(Node *L1, Node *L2) {
        Node *newList = mergeRootLists(L1, L2);
        if (newList == nullptr) return nullptr;

        Node *prev = nullptr;
        Node *curr = newList;
        Node *next = curr->immediateRightSibling;

        while (next != nullptr) {
            if (curr->degree != next->degree || (next->immediateRightSibling != nullptr &&
                                                 next->immediateRightSibling->degree == curr->degree)) {
                prev = curr;
                curr = next;
            } else {
                if (curr->key <= next->key) {
                    curr->immediateRightSibling = next->immediateRightSibling;
                    linkTrees(next, curr);
                } else {
                    if (prev != nullptr)
                        prev->immediateRightSibling = next;
                    else
                        newList = next;
                    linkTrees(curr, next);
                    curr = next;
                }
            }
            next = curr->immediateRightSibling;
        }
        return newList;
    }

    [[nodiscard]] Node *findMinNode() const {
        if (head == nullptr) return nullptr;

        Node *minNode = head;
        Node *curr = head->immediateRightSibling;

        while (curr != nullptr) {
            if (curr->key < minNode->key)
                minNode = curr;
            curr = curr->immediateRightSibling;
        }

        return minNode;
    }

    [[nodiscard]] int getMinKey() const {
        const Node *minNode = findMinNode();
        if (minNode == nullptr) {
            cout << "Heap is empty\n";
            return 0;
        }
        return minNode->key;
    }

    int extractMin() {
        if (head == nullptr) {
            cout << "Heap is empty";
            return 0;
        }

        //Find min Node and the one before
        Node *prevMin = nullptr;
        Node *minNode = head;
        Node *prev = nullptr;
        Node *curr = head;

        int minKey = curr->key;
        while (curr != nullptr) {
            if (curr->key < minKey) {
                minKey = curr->key;
                prevMin = prev;
                minNode = curr;
            }
            prev = curr;
            curr = curr->immediateRightSibling;
        }

        //Delete min Node from list
        if (prevMin != nullptr)
            prevMin->immediateRightSibling = minNode->immediateRightSibling;
        else
            head = minNode->immediateRightSibling;

        //Reverse the list order of the children of the deleted Node
        Node *child = minNode->leftmostChild;
        Node *reversed = nullptr;

        while (child != nullptr) {
            Node *next = child->immediateRightSibling;
            child->immediateRightSibling = reversed;
            child->parent = nullptr;
            reversed = child;
            child = next;
        }

        // Merge with the remaining heap
        Node *tempHeap = reversed;
        head = unionHeap(head, tempHeap);

        int minValue = minNode->key;
        delete minNode;
        return minValue;
    }

    void insert(const int key) {
        Node *newNode = new Node(key);
        head = unionHeap(head, newNode);
    }

    static Node *findNode(Node *root, int key) {
        if (root == nullptr) return nullptr;
        if (root->key == key) return root;

        Node *child = root->leftmostChild;
        while (child) {
            Node *found = findNode(child, key);
            if (found) return found;
            child = child->immediateRightSibling;
        }

        return findNode(root->immediateRightSibling, key);
    }

    static void goUp(Node* node) {
        while (node->parent && node->key < node->parent->key) {
            swap(node->key, node->parent->key);
            node = node->parent;
        }
    }

    void deleteNode(const int key) {
        Node *Node = findNode(head, key);
        if (Node == nullptr) return;
        Node->key = -1000000;
        goUp(Node);
        extractMin();
    }

    static void printTree(Node *node, int indent) {
        if (node == nullptr) return;

        for (int i = 0; i < indent; ++i)
            cout << "  ";

        cout << node->key << " (degree " << node->degree << ")\n";

        Node *child = node->leftmostChild;
        while (child) {
            printTree(child, indent + 1);
            child = child->immediateRightSibling;
        }
    }

    void print() const {
        if (!head) {
            cout << "Heap is empty.\n";
            return;
        }

        cout << "Binomial Heap:\n";
        Node *curr = head;
        int treeNum = 0;

        while (curr) {
            cout << "Tree " << treeNum++ << " (B" << curr->degree << "):\n";
            printTree(curr, 1);
            cout << "\n";
            curr = curr->immediateRightSibling;
        }
    }
};

int main() {
    BinomialHeap heap;
    heap.print();
    cout << heap.getMinKey() << endl;
    cout << endl;
    heap.insert(5);
    heap.print();
    cout << heap.getMinKey() << endl;
    heap.insert(7);
    heap.insert(8);
    heap.insert(9);
    heap.insert(10);
    heap.print();
    cout << heap.getMinKey() << endl;
    heap.insert(11);
    heap.insert(12);
    heap.print();
    cout << heap.getMinKey() << endl;
    heap.insert(13);
    heap.print();
    cout << heap.getMinKey() << endl;
    heap.extractMin();
    heap.print();
    cout << heap.extractMin() << endl;
    heap.print();
    heap.insert(42);
    heap.insert(43);
    heap.print();
    heap.deleteNode(12);
    heap.print();
    return 0;
}
