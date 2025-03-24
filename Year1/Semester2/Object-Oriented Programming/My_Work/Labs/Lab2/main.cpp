#include <iostream>
#include <cmath>
#include <vector>
using namespace std;

class Polinom {
    vector<int> polinom;
public:
    Polinom() = default;

    friend istream &operator>>(istream &in, Polinom &x) {
        int n;
        cout << "Introduceti gradul maxim: ";
        in >> n;
        x.polinom.resize(n);
        cout << "Introduceti coeficientii: ";
        for (int i = n; i >= 0; i--) {
            in >> x.polinom[i];
        }
        return in;
    }

    friend ostream &operator<<(ostream &out, const Polinom &x) {
        for (int i = x.polinom.size(); i >= 0; i--) {
            if (x.polinom[i] != 0) {
                out << x.polinom[i];
                if (i != 0) {
                    out << "x^" << i << " + ";
                }
            }
        }
        return out;
    }

    Polinom operator+(const Polinom &y) {
        Polinom p;
        int aux_min = min(this->polinom.size(), y.polinom.size());
        int aux_max = max(this->polinom.size(), y.polinom.size());
        p.polinom.resize(aux_max);
        for (int i = 0; i <= aux_min; i++) {
            p.polinom[i] = this->polinom[i] + y.polinom[i];
        }
        for (int i = aux_min+1; i <= aux_max; i++) {
            if (this->polinom.size() > y.polinom.size()) {
                p.polinom[i] = this->polinom[i];
            } else {
                p.polinom[i] = y.polinom[i];
            }
        }
        return p;
    }


};

int main(){
    Polinom p1, p2;
    // cout << "Introduceti polinomul: \n";
    // cin >> p1;
    // cout << p1;
    cin >> p1 >> p2;
    cout << p1 + p2;
    return 0;
}