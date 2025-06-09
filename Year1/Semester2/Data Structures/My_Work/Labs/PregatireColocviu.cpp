#include <iostream>
#include <stack>
#include <deque>
#include <queue>
#include <vector>
#include <functional>
#include <set>
#include <unordered_map>
#include <string>

int main() {
    //     std::cout<<"STACK"<<std::endl<<std::endl;
    //     std::stack<int> stack;
    //     if (!stack.empty())std::cout<<stack.top()<<std::endl;
    //     else std::cout<<"STACK IS EMPTY"<<std::endl;
    //     stack.push(10);
    //     if (!stack.empty())std::cout<<stack.top()<<std::endl;
    //     else std::cout<<"STACK IS EMPTY"<<std::endl;
    //     if (!stack.empty())std::cout<<stack.top()<<std::endl;
    //     else std::cout<<"STACK IS EMPTY"<<std::endl;
    //     stack.pop();
    //     if (!stack.empty())std::cout<<stack.top()<<std::endl;
    //     else std::cout<<"STACK IS EMPTY"<<std::endl<<std::endl;
    //
    //     std::cout<<"DEQUE"<<std::endl<<std::endl;
    //     std::deque<int> dq;
    //     if (!dq.empty()) {
    //         std::cout<<"Front: "<<dq.front()<<std::endl;
    //         std::cout<<"Back: "<<dq.back()<<std::endl;
    //     }
    //     else std::cout<<"DEQUE IS EMPTY"<<std::endl<<std::endl;
    //     dq.push_front(10);
    //     if (!dq.empty()) {
    //         std::cout<<"Front: "<<dq.front()<<std::endl;
    //         std::cout<<"Back: "<<dq.back()<<std::endl;
    //     }
    //     else std::cout<<"DEQUE IS EMPTY"<<std::endl<<std::endl;
    //     dq.push_front(20);
    //     if (!dq.empty()) {
    //         std::cout<<"Front: "<<dq.front()<<std::endl;
    //         std::cout<<"Back: "<<dq.back()<<std::endl;
    //     }
    //     else std::cout<<"DEQUE IS EMPTY"<<std::endl<<std::endl;
    //     dq.push_back(30);
    //     if (!dq.empty()) {
    //         std::cout<<"Front: "<<dq.front()<<std::endl;
    //         std::cout<<"Back: "<<dq.back()<<std::endl;
    //     }
    //     else std::cout<<"DEQUE IS EMPTY"<<std::endl<<std::endl;
    //     dq.pop_front();
    //     if (!dq.empty()) {
    //         std::cout<<"Front: "<<dq.front()<<std::endl;
    //         std::cout<<"Back: "<<dq.back()<<std::endl;
    //     }
    //     else std::cout<<"DEQUE IS EMPTY"<<std::endl<<std::endl;
    //     dq.pop_back();
    //     if (!dq.empty()) {
    //         std::cout<<"Front: "<<dq.front()<<std::endl;
    //         std::cout<<"Back: "<<dq.back()<<std::endl;
    //     }
    //     else std::cout<<"DEQUE IS EMPTY"<<std::endl<<std::endl;
    //     dq.pop_front();
    //     if (!dq.empty()) {
    //         std::cout<<"Front: "<<dq.front()<<std::endl;
    //         std::cout<<"Back: "<<dq.back()<<std::endl;
    //     }
    //     else std::cout<<"DEQUE IS EMPTY"<<std::endl<<std::endl;

    // std::priority_queue<int> maxheap; /////radacina e cea mai mare
    // std::cout<<"MAX HEAP"<<std::endl;
    // if (!maxheap.empty()) std::cout<<maxheap.top()<<std::endl;
    // else std::cout<<"HEAP IS EMPTY"<<std::endl;
    //
    // maxheap.push(10);
    // if (!maxheap.empty()) std::cout<<maxheap.top()<<std::endl;
    // else std::cout<<"HEAP IS EMPTY"<<std::endl;
    //
    // maxheap.push(5);
    // if (!maxheap.empty()) std::cout<<maxheap.top()<<std::endl;
    // else std::cout<<"HEAP IS EMPTY"<<std::endl;
    //
    // maxheap.push(20);
    // if (!maxheap.empty()) std::cout<<maxheap.top()<<std::endl<<std::endl;
    // else std::cout<<"HEAP IS EMPTY"<<std::endl<<std::endl;
    //
    // std::cout<<std::endl;
    //
    // if (!maxheap.empty()) {
    //     maxheap.pop();
    //     if (!maxheap.empty()) {
    //         std::cout << maxheap.top() << std::endl;
    //     }
    // }
    // else std::cout<<"HEAP IS EMPTY"<<std::endl;
    //
    // if (!maxheap.empty()) {
    //     maxheap.pop();
    //     if (!maxheap.empty()) {
    //         std::cout << maxheap.top() << std::endl;
    //     }
    // }
    // else std::cout<<"HEAP IS EMPTY"<<std::endl;
    //
    // if (!maxheap.empty()) {
    //     maxheap.pop();
    //     if (!maxheap.empty()) {
    //         std::cout << maxheap.top() << std::endl;
    //     }
    // }
    // else std::cout<<"HEAP IS EMPTY"<<std::endl;
    //
    // if (!maxheap.empty()) {
    //     maxheap.pop();
    //     if (!maxheap.empty()) {
    //         std::cout << maxheap.top() << std::endl;
    //     }
    // }
    // else std::cout<<"HEAP IS EMPTY"<<std::endl;
    //
    // if (!maxheap.empty()) {
    //     maxheap.pop();
    //     if (!maxheap.empty()) {
    //         std::cout << maxheap.top() << std::endl;
    //     }
    // }
    // else std::cout<<"HEAP IS EMPTY"<<std::endl;
    //
    //
    //
    //
    // std::cout<<std::endl<<"MIN HEAP"<<std::endl<<std::endl;
    // std::priority_queue<int, std::vector<int>, std::greater<>> minheap;
    //
    // if (!minheap.empty()) std::cout<<minheap.top()<<std::endl;
    // else std::cout<<"HEAP IS EMPTY"<<std::endl;
    //
    // minheap.push(10);
    // if (!minheap.empty()) std::cout<<minheap.top()<<std::endl;
    // else std::cout<<"HEAP IS EMPTY"<<std::endl;
    //
    // minheap.push(5);
    // if (!minheap.empty()) std::cout<<minheap.top()<<std::endl;
    // else std::cout<<"HEAP IS EMPTY"<<std::endl;
    //
    // minheap.push(20);
    // if (!minheap.empty()) std::cout<<minheap.top()<<std::endl<<std::endl;
    // else std::cout<<"HEAP IS EMPTY"<<std::endl<<std::endl;
    //
    // if (!minheap.empty()) {
    //     minheap.pop();
    //     if (!minheap.empty()) {
    //         std::cout << minheap.top() << std::endl;
    //     }
    // }
    // else std::cout<<"HEAP IS EMPTY"<<std::endl;
    //
    // if (!minheap.empty()) {
    //     minheap.pop();
    //     if (!minheap.empty()) {
    //         std::cout << minheap.top() << std::endl;
    //     }
    // }
    // else std::cout<<"HEAP IS EMPTY"<<std::endl;
    //
    // if (!minheap.empty()) {
    //     minheap.pop();
    //     if (!minheap.empty()) {
    //         std::cout << minheap.top() << std::endl;
    //     }
    // }
    // else std::cout<<"HEAP IS EMPTY"<<std::endl;
    //
    // if (!minheap.empty()) {
    //     minheap.pop();
    //     if (!minheap.empty()) {
    //         std::cout << minheap.top() << std::endl;
    //     }
    // }
    // else std::cout<<"HEAP IS EMPTY"<<std::endl;
    //
    // if (!minheap.empty()) {
    //     minheap.pop();
    //     if (!minheap.empty()) {
    //         std::cout << minheap.top() << std::endl;
    //     }
    // }
    // else std::cout<<"HEAP IS EMPTY"<<std::endl;

    //EX 1 MODEL COLOCVIU
    // std::priority_queue<int, std::vector<int>, std::greater<> > minheap;
    // int n, k, x, cnt = 0;
    //
    // std::cin >> n >> k;
    //
    // while (n) {
    //     std::cin >> x;
    //     n--;
    //
    //     if (cnt < k) {
    //         minheap.push(x);
    //         cnt++;
    //     }
    //     else if (minheap.top() < x) {
    //         minheap.pop();
    //         minheap.push(x);
    //     }
    // }
    //
    // std::vector<int> rezultat;
    // while (!minheap.empty()) {
    //     rezultat.push_back(minheap.top());
    //     minheap.pop();
    // }
    //
    // for (int i = rezultat.size() - 1; i >=0;i--)
    //     std::cout<<rezultat[i]<<" ";

    //BST (SET)
    // std::set<int> bst;
    // bst.insert(5);
    // bst.insert(10);
    // bst.insert(5);
    //
    // std::cout << "\nSET: \n";
    // for (int i: bst) {
    //     std::cout << i << " ";
    // }
    //
    // if (bst.find(5) != bst.end()) {
    //     std::cout<<"EXISTA!\n";
    // }
    // else std::cout<<"Nu exista!\n";
    //
    // if (bst.find(4) != bst.end()) {
    //     std::cout<<"EXISTA!\n";
    // }
    // else std::cout<<"Nu exista!\n";
    //
    // std::cout<<std::endl<<bst.size()<<std::endl;
    //
    // bst.erase(13);
    //
    // std::cout << "\nSET: \n";
    // for (int i: bst) {
    //     std::cout << i << " ";
    // }
    //
    // bst.erase(10);
    //
    // std::cout << "\nSET: \n";
    // for (int i: bst) {
    //     std::cout << i << " ";
    // }
    //
    // std::cout<<std::endl<<bst.size()<<std::endl;

    //EX 2 MODEL COLOCVIU

    // int n, k, v;
    // std::cin >> n;
    //
    // std::set<int> bst;
    //
    // while (n) {
    //     n--;
    //
    //     //Adauga = 1, Cauta = 2, Arata = 3
    //     std::cin >> k;
    //     if (k == 1) {
    //         std::cin >> v;
    //         bst.insert(v);
    //     }
    //     if (k == 2) {
    //         std::cin >> v;
    //         if (bst.find(v) != bst.end()) {
    //             std::cout << "DA\n";
    //         } else std::cout << "Nu\n";
    //     }
    //     if (k == 3) {
    //         for (int i: bst) {
    //             std::cout << i << " ";
    //         }
    //     }
    // }

    std::unordered_map<std::string, std::string> tit_cat;
    std::unordered_map<std::string, int> tit_num;
    int n, x, k;
    std::string t, c;
    std::cin >> n;

    while (n) {
        n--;
        //1=add,2=remove,3=check,4=count
        std::cin >> x;
        if (x == 1) {
            std::cin >> t >> c >> k;
            if (tit_cat.find(t) == tit_cat.end()) {
                tit_cat[t] = c;
                tit_num[t] = k;
            } else if (tit_cat[t] == c) {
                tit_num[t] += k;
            }
            else std::cout<< "INVALID\n";
        }
        if (x == 2) {
            std::cin>>t>>k;
            tit_num[t] -=k;
            if (tit_num[t] == 0) {
                tit_num.erase(t);
                tit_cat.erase(t);
            }
        }
        if (x==3) {
            std::cin>>t;
            if (tit_cat.find(t) != tit_cat.end()) {
                std::cout<<tit_cat[t]<<"\n";
            }
            else std::cout<<"NU\n";
        }
        if (x==4) {
            std::cin>>c;
            if (tit_cat.find(t) == tit_cat.end()) {
                std::cout<<0;
            }
            else std::cout<<tit_num[t];
        }
    }

    return 0;
}
