#include <iostream>
#include <stack>
#include <deque>
#include <queue>
#include <set>
#include <unordered_map>
#include <vector>
#include <string>

using namespace std;

int main() {
    //EX 1
    // int n, k, cnt = 0, x;
    // cin >> n >> k;
    // priority_queue<int, vector<int>, greater<> > minheap;
    //
    // while (n) {
    //     n--;
    //     cin >> x;
    //     if (cnt < k) {
    //         cnt++;
    //         minheap.push(x);
    //     }
    //     else {
    //         if (minheap.top()<x) {
    //             minheap.pop();
    //             minheap.push(x);
    //         }
    //     }
    // }
    //
    // while (!minheap.empty()) {
    //     cout<<minheap.top()<< " ";
    //     minheap.pop();
    // }

    // EX2
    //  set<int> bst;
    //  int op, n, x;
    //  cin >> n;
    //  while (n) {
    //      n--;
    //      cin >> op;
    //      if (op == 0) {
    //          cin >> x;
    //          bst.insert(x);
    //      }
    //      if (op == 1) {
    //          cin >> x;
    //          if (bst.find(x) != bst.end()) {
    //              cout << "DA\n";
    //          } else {
    //              cout << "NU\n";
    //          }
    //      }
    //      if (op == 2) {
    //          for (int i: bst) {
    //              cout << i << " ";
    //          }
    //          cout << endl;
    //      }
    //  }


    //EX3
    unordered_map<string, pair<string, int>> nume_cat_numar;
    unordered_map<string, int> cat_numar;
    int n, Q;
    string k, N, T;
    cin >> n;
    while (n) {
        n--;
        cin >> k;
        if (k == "ADD") {
            cin >> N >> T >> Q;
            if (nume_cat_numar.find(N) == nume_cat_numar.end()) {
                nume_cat_numar[N] = pair(T, Q);
                if (cat_numar.find(T) == cat_numar.end()) {
                    cat_numar[T] = Q;
                }
                else cat_numar[T] += Q;
            } else
                if (T != nume_cat_numar[N].first) cout << "INVALID\n";
                else {
                    nume_cat_numar[N].second += Q;
                    cat_numar[T] += Q;
                }
        }
        if (k == "REMOVE") {
            cin >> N >> Q;
            nume_cat_numar[N].second -= Q;
            cat_numar[nume_cat_numar[N].first] -= Q;
            if (nume_cat_numar[N].second <= 0) {
                nume_cat_numar.erase(N);
            }
            if (cat_numar[N] <= 0) {
                cat_numar.erase(N);
            }
        }
        if (k == "CHECK") {
            cin >> N;
            if (nume_cat_numar.find(N) != nume_cat_numar.end()) {
                cout << nume_cat_numar[N].first << endl;
            } else cout << "NU\n";
        }
        if (k == "COUNT") {
            cin >> T;
            cout << cat_numar[T] << endl;
        }
    }

    return 0;
}
