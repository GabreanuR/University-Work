#include <iostream>
#include <cmath>

using namespace std;

class numarComplex {
    int pInt, pFra;

public:
    numarComplex() = default;

    numarComplex(const numarComplex &x) {
        this->pInt = x.pInt;
        this->pFra = x.pFra;
    }

    numarComplex(int pInt, int pFra): pInt(pInt), pFra(pFra) {
    }

    // numarComplex(int pInt, int pFra){
    //     this->pInt = pInt;
    //     this->pFra = pFra;
    // }

    ~numarComplex() {
        cout << "Destructor called " << pInt << endl;
    }

    numarComplex &operator=(const numarComplex &x) {
        if (this != &x) {
            this->pInt = x.pInt;
            this->pFra = x.pFra;
        }
        return *this;
    }

    friend istream &operator>>(istream &in, numarComplex &x) {
        in >> x.pInt >> x.pFra;
        return in;
    }

    friend ostream &operator<<(ostream &out, const numarComplex &x) {
        out << x.pInt << " " << x.pFra << endl;
        return out;
    }

    // friend numarComplex operator+(const numarComplex &x, const numarComplex &y) {
    //     numarComplex z;
    //     z.pInt = x.pInt + y.pInt;
    //     z.pFra = x.pFra + y.pFra;
    //     return z;
    // }

    numarComplex operator+(const numarComplex &y) {
        numarComplex z;
        z.pInt = this->pInt + y.pInt;
        z.pFra = this->pFra + y.pFra;
        return z;
    }

    float modul() const {
        return sqrt(this->pInt * this->pInt + this->pFra * this->pFra);
    }
};

int main() {
    // numarComplex a;
    // numarComplex b(a);
    // numarComplex c(1, 2);
    // c = a;
    //
    // cin >> a;
    // // cin >> b;
    // // cout << a + b;
    //
    // cout<<a.modul()<<endl;;
    //
    // // int y, z;
    // // cin >> y >> z;
    // // cout << y + z << endl;

    numarComplex c(1, 2);
    cout<<c.modul()<<endl;

    const numarComplex d(1, 2);
    cout<<d.modul()<<endl;

    return 0;
}
