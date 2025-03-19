#include <iostream>
#include <fstream>
using namespace std;

//2746 PBINFO

// int heap[1000000];
// int dim;
//
// void up(int pos) {
//     if (heap[pos] < heap[(pos - 1) / 2]) {
//         swap(heap[pos], heap[(pos - 1) / 2]);
//         up((pos - 1) / 2);
//     }
// }
//
// void inserare(int nr) {
//     heap[dim] = nr;
//     dim++;
//     up(dim - 1);
// }
//
// void down(int pos) {
//     if (pos * 2 + 2 < dim) {
//         int minim = min(heap[pos * 2 + 1], heap[pos * 2 + 2]);
//         if (minim > heap[pos])return;
//         if (minim == heap[pos * 2 + 1]) {
//             swap(heap[pos], heap[pos * 2 + 1]);
//             down(pos * 2 + 1);
//         } else {
//             swap(heap[pos], heap[pos * 2 + 2]);
//             down(pos * 2 + 2);
//         }
//     } else if (pos * 2 + 1 < dim && heap[pos] > heap[pos * 2 + 1]) {
//         swap(heap[pos], heap[pos * 2 + 1]);
//     }
// }
//
// int extragere() {
//     int r = heap[0];
//     swap(heap[0], heap[dim - 1]);
//     dim--;
//     down(0);
//     return r;
// }
//
// void build() {
//     for (int i = (dim - 1) / 2; i >= 0; i--) {
//         down(i);
//     }
// }
//
// int main() {
//     ifstream fin("heap_sort.in");
//     ofstream fout("heap_sort.out");
//     int x, y;
//     fin >> dim;
//     // for (int i = 0; i < x; i++) {
//     //     cin >> y;
//     //     inserare(y);
//     // }
//     for (int i = 0; i < dim; i++) {
//         fin >> heap[i];
//     }
//     build();
//     // for (int i = 0; i < dim; i++) {
//     //     cout << heap[i] << " ";
//     // }
//     // cout << endl;
//     while (dim) {
//         fout << extragere() << " ";
//     }
//     fout << endl;
//
//     fin.close();
//     fout.close();
//     return 0;
// }

// 3011 PBINFO

int heap[100001];
int dim;

void up(int pos) {
    if (heap[pos] < heap[(pos - 1) / 2]) {
        swap(heap[pos], heap[(pos - 1) / 2]);
        up((pos - 1) / 2);
    }
}

void inserare(int nr) {
    heap[dim] = nr;
    dim++;
    up(dim - 1);
}

void down(int pos) {
    if (pos * 2 + 2 < dim) {
        int minim = min(heap[pos * 2 + 1], heap[pos * 2 + 2]);
        if (minim > heap[pos])return;
        if (minim == heap[pos * 2 + 1]) {
            swap(heap[pos], heap[pos * 2 + 1]);
            down(pos * 2 + 1);
        } else {
            swap(heap[pos], heap[pos * 2 + 2]);
            down(pos * 2 + 2);
        }
    } else if (pos * 2 + 1 < dim && heap[pos] > heap[pos * 2 + 1]) {
        swap(heap[pos], heap[pos * 2 + 1]);
    }
}

int extragere() {
    int r = heap[0];
    swap(heap[0], heap[dim - 1]);
    dim--;
    down(0);
    return r;
}

void build() {
    for (int i = (dim - 1) / 2; i >= 0; i--) {
        down(i);
    }
}

int main() {
    int n, k, A, B, C, D, aux;
    cin >> n >> k >> A >> B >> C >> D;
    aux = A;
    for (int i = 0; i < n; i++) {
        inserare(aux);
        aux = (B * aux + C) % D;
        if (i >= k) {
            extragere();
        }
    }
    build();
    for (int i = 0; i < k; i++) {
        cout << extragere() << " ";
    }
    return 0;
}
